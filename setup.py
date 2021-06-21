#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='MASCADO',
    version='1.0',
    description='Inspection tool for Mask Astrometry data '
                'from the MICADO project.',
    author='Hannes Riechert',
    author_email='hannes@tychons.net',
    python_requires='>=3.5',
    url='https://github.com/tychon/mascado',
    license='GPLv3',

    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=[
        'numpy>=1.14',
        'matplotlib',
        'scipy',
        'pandas',
        'pytest',
        'pytest-cov'],
    scripts=[
        'scripts/mascado_analyze',
        'scripts/mascado_compare'],
    test_suite='tests',
)
