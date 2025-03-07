#!/usr/bin/env python

from setuptools import setup, find_packages
import pysensorsdata
import versioneer  # noqa

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name="pysensorsdata",
    version=pysensorsdata.__version__,
    #cmdclass=versioneer.get_cmdclass(),
    description="Python interface to SensorsData DataWarehouse",
    long_description=long_description,
    url='https://sensorsdata.com/',
    author="Chen Wang",
    author_email="wangchen@sensorsdata.com",
    packages=find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires=[
        'future',
        'python-dateutil',
        'thrift>=0.10.0',
        'thrift_sasl>=0.1.0',
    ],
    extras_require={
        'sqlalchemy': ['sqlalchemy>=1.3.0'],
        'kerberos': ['requests_kerberos>=0.12.0'],
    },
    package_data={
        '': ['*.md'],
    },
    entry_points={
        'sqlalchemy.dialects': [
            'sensorsdata = pysensorsdata.sqlalchemy:SensorsDataDialect',
        ],
    }
)
