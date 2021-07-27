# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pav_balanced_scorecard/__init__.py
from pav_balanced_scorecard import __version__ as version

setup(
	name='pav_balanced_scorecard',
	version=version,
	description='Partner ERPNext - Add Value On Balanced Scorecard',
	author='Farouk Muharram',
	author_email='Farouk1dev@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
