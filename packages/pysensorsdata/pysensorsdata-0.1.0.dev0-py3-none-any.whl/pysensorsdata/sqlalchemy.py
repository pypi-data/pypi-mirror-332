"""Integration between SQLAlchemy and Horizon.
"""

from __future__ import absolute_import
from __future__ import unicode_literals

import datetime
import decimal

import re
from sqlalchemy import exc
from sqlalchemy.sql import text

try:
    from sqlalchemy import processors
except ImportError:
    # Required for SQLAlchemy>=2.0
    from sqlalchemy.engine import processors
from sqlalchemy import types
from sqlalchemy import util

# TODO shouldn't use mysql type
try:
    from sqlalchemy.databases import mysql

    mysql_tinyinteger = mysql.MSTinyInteger
except ImportError:
    # Required for SQLAlchemy>2.0
    from sqlalchemy.dialects import mysql

    mysql_tinyinteger = mysql.base.MSTinyInteger
from sqlalchemy.engine import default
from sqlalchemy.sql import compiler
from sqlalchemy.sql.compiler import SQLCompiler

from pysensorsdata import hive
from pysensorsdata.common import UniversalSet


class HiveIdentifierPreparer(compiler.IdentifierPreparer):
    # Just quote everything to make things simpler / easier to upgrade
    reserved_words = UniversalSet()

    def __init__(self, dialect):
        super(HiveIdentifierPreparer, self).__init__(
            dialect,
            initial_quote='`',
        )


_type_map = {
    'boolean': types.Boolean,
    'tinyint': types.Integer,
    'smallint': types.SmallInteger,
    'int': types.Integer,
    'bigint': types.BigInteger,
    'float': types.Float,
    'double': types.DOUBLE,
    'number': types.DOUBLE,
    'string': types.String,
    'varchar': types.String,
    'char': types.String,
    'date': types.DATE,
    'timestamp': types.TIMESTAMP,
    'binary': types.String,
    'array': types.String,
    'map': types.String,
    'struct': types.String,
    'uniontype': types.String,
    'decimal': types.DECIMAL,
    'array<bytes>': types.ARRAY,
}


class HiveCompiler(SQLCompiler):
    def visit_concat_op_binary(self, binary, operator, **kw):
        return "concat(%s, %s)" % (self.process(binary.left), self.process(binary.right))

    def visit_insert(self, *args, **kwargs):
        result = super(HiveCompiler, self).visit_insert(*args, **kwargs)
        # Massage the result into Hive's format
        #   INSERT INTO `pyhive_test_database`.`test_table` (`a`) SELECT ...
        #   =>
        #   INSERT INTO TABLE `pyhive_test_database`.`test_table` SELECT ...
        regex = r'^(INSERT INTO) ([^\s]+) \([^\)]*\)'
        assert re.search(regex, result), "Unexpected visit_insert result: {}".format(result)
        return re.sub(regex, r'\1 TABLE \2', result)

    def visit_column(self, *args, **kwargs):
        result = super(HiveCompiler, self).visit_column(*args, **kwargs)
        dot_count = result.count('.')
        assert dot_count in (0, 1, 2), "Unexpected visit_column result {}".format(result)
        if dot_count == 2:
            # we have something of the form schema.table.column
            # hive doesn't like the schema in front, so chop it out
            result = result[result.index('.') + 1:]
        return result

    def visit_char_length_func(self, fn, **kw):
        return 'length{}'.format(self.function_argspec(fn, **kw))


class HiveTypeCompiler(compiler.GenericTypeCompiler):
    # pylint: disable=unused-argument

    def visit_TINYINT(self, type_):
        return 'TINYINT'

    def visit_INT(self, type_):
        return 'INT'

    def visit_INTEGER(self, type_):
        return 'INT'

    def visit_NUMERIC(self, type_):
        return 'DECIMAL'

    def visit_CHAR(self, type_):
        return 'STRING'

    def visit_VARCHAR(self, type_):
        return 'STRING'

    def visit_NCHAR(self, type_):
        return 'STRING'

    def visit_TEXT(self, type_):
        return 'STRING'

    def visit_CLOB(self, type_):
        return 'STRING'

    def visit_BLOB(self, type_):
        return 'BINARY'

    def visit_TIME(self, type_):
        return 'TIMESTAMP'

    def visit_DATE(self, type_):
        return 'TIMESTAMP'

    def visit_DATETIME(self, type_):
        return 'TIMESTAMP'

    visit_NVARCHAR = visit_TEXT

    def visit_DOUBLE(self, type_):
        return 'DOUBLE'

    def visit_STRING(self, type_):
        return 'STRING'


class HiveExecutionContext(default.DefaultExecutionContext):
    """This is pretty much the same as SQLiteExecutionContext to work around the same issue.

    http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#dotted-column-names

    engine = create_engine('hive://...', execution_options={'hive_raw_colnames': True})
    """

    @util.memoized_property
    def _preserve_raw_colnames(self):
        # Ideally, this would also gate on hive.resultset.use.unique.column.names
        return self.execution_options.get('hive_raw_colnames', False)

    def _translate_colname(self, colname):
        # Adjust for dotted column names.
        # When hive.resultset.use.unique.column.names is true (the default), Hive returns column
        # names as "tablename.colname" in cursor.description.
        if not self._preserve_raw_colnames and '.' in colname:
            return colname.split('.')[-1], colname
        else:
            return colname, None


class SensorsDataDialect(default.DefaultDialect):
    name = 'sensorsdata'
    driver = 'thrift'
    execution_ctx_cls = HiveExecutionContext
    preparer = HiveIdentifierPreparer
    statement_compiler = HiveCompiler
    supports_views = True
    supports_alter = True
    supports_pk_autoincrement = False
    supports_default_values = False
    supports_empty_insert = False
    supports_native_decimal = True
    supports_native_boolean = True
    supports_unicode_statements = True
    supports_unicode_binds = True
    returns_unicode_strings = True
    description_encoding = None
    supports_multivalues_insert = True
    type_compiler = HiveTypeCompiler
    supports_sane_rowcount = False
    supports_statement_cache = False

    @classmethod
    def dbapi(cls):
        return hive

    @classmethod
    def import_dbapi(cls):
        return hive

    def create_connect_args(self, url):
        kwargs = {
            'host': url.host,
            'port': url.port or 10000,
            'username': url.username,
            'password': url.password,
            'database': url.database or 'default',
        }
        kwargs.update(url.query)
        return [], kwargs

    def get_schema_names(self, connection, **kw):
        # Equivalent to SHOW DATABASES
        return [row[0] for row in connection.execute(text('SHOW SCHEMAS'))]

    def get_view_names(self, connection, schema=None, **kw):
        # Hive does not provide functionality to query tableType
        # This allows reflection to not crash at the cost of being inaccurate
        return self.get_table_names(connection, schema, **kw)

    def has_table(self, connection, table_name, schema=None, **kw):
        tables = self.get_table_names(connection, schema)
        if table_name in tables:
            return True
        return False

    def get_columns(self, connection, table_name, schema=None, **kw):
        # pylint: disable=unused-argument
        name = table_name
        if schema is not None:
            name = '%s.%s' % (schema, name)
        cursor = connection.execute(text(f"DESCRIBE {name}"))
        column_names = [desc[0].lower() for desc in cursor.cursor.description]
        fields_to_find = ['name', 'type', 'null', 'nullable', 'primary_key', 'comment']
        field_indices = {field: column_names.index(field) if field in column_names else -1 for field in fields_to_find}

        # We need to fetch the empty results otherwise these queries remain in
        # flight
        rows = cursor.fetchall()
        column_info = []
        for row in rows:
            col_name = row[field_indices['name']].strip()
            type_str = str(row[field_indices['type']]).lower()
            if type_str.startswith('array'):
                col_type = _type_map.get('array')
            else:
                col_type = _type_map.get(type_str, 'unknown')
            nullable_index = field_indices.get('null', -1)
            if nullable_index == -1:
                nullable_index = field_indices.get('nullable', -1)
            col_nullable = bool(row[nullable_index]) if nullable_index != -1 else True

            col_key = bool(row[field_indices['primary_key']]) if field_indices['primary_key'] != -1 else False
            col_comment = row[field_indices['comment']] if field_indices['comment'] != -1 else ''

            column_info.append({
                'name': col_name,
                'type': col_type,
                'nullable': col_nullable,
                'primary_key': col_key,
                'comment': col_comment,
            })
        return column_info

    def get_foreign_keys(self, connection, table_name, schema=None, **kw):
        # Hive has no support for foreign keys.
        return []

    def get_pk_constraint(self, connection, table_name, schema=None, **kw):
        # Hive has no support for primary keys.
        return []

    def get_indexes(self, connection, table_name, schema=None, **kw):
        # no indexes in impala
        # TODO(laserson): handle partitions, like in PyHive
        return []

    def get_table_names(self, connection, schema=None, **kw):
        query = 'SHOW TABLES'
        if schema:
            query += ' IN ' + self.identifier_preparer.quote_identifier(schema)
        tables = [row[0] for row in connection.execute(text(query))]
        return [s for s in tables if not s.startswith('sessions_')]

    def do_rollback(self, dbapi_connection):
        # No transactions for Hive
        pass

    def _check_unicode_returns(self, connection, additional_tests=None):
        # We decode everything as UTF-8
        return True

    def _check_unicode_description(self, connection):
        # We decode everything as UTF-8
        return True

