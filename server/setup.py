#! /usr/bin/env python2.7

from setuptools import setup

setup(
    name='rest_api',
    version='0.0.1',
    packages=['rest_api'],
    include_package_data=True,
    install_requires=[
        'Flask==1.0.2',
        'bcrypt==3.1.4',
        'requests==2.20.1'
    ],
)
