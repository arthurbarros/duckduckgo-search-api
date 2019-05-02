#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    requirements = [req.strip() for req in f.readlines()]

setup(name='duckduckgo-search-api',
      version='1.0.0',
      url='https://github.com/arthurbarros/duckduckgo-search-api',
      description='Search in duckduckgo',
      author='Arthur Barros',
      author_email='arthbarros@gmail.com',
      maintainer='Arthur Barros',
      maintainer_email='arthbarros@gmail.com',
      license='MIT',
      packages=[
          'duckduckgo',
          'duckduckgo.modules'
      ],
      package_dir={'duckduckgo': 'duckduckgo'},
      include_package_data=True,
      install_requires=requirements,
      keywords='duckduckgo search images api',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ])
