from setuptools import setup, find_packages
import os

setup(
name = 'labbu',
version = '1.0.2',
author = 'Tyler Koziol',
description = 'Tool to make contextual editing of HTK-style lab files more intuitive and user friendly.',
packages = find_packages(where='labbu'),
py_module = ['labbu', '__init__'],
install_requires = ['mytextgrid', 'PyYAML', 'ftfy', 'loguru'],
scripts = [
	'labbu/labbu.py',
	'labbu/__init__.py',
	'labbu/modules/__init__.py',
	'labbu/modules/label.py',	
],
include_package_data = True,
package_dir = {"": "labbu"},
classifiers=[
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
	'Operating System :: OS Independent',
],
)