
import setuptools
from distutils.core import setup
import sys
import time
setup(
	# Application name:
	name="ChromeController",

	# Version number (initial):
	version="0.1.6",

	# Application author details:
	author="Connor Wolf	",
	author_email="github@imaginaryindustries.com",

	# Packages
	packages=setuptools.find_packages(),
	package_dir = {'ChromeController': 'ChromeController'},

	# Bundle the protocol json files.
	package_data={'ChromeController': ['protocols/*.json']},

	# Details
	url="https://github.com/fake-name/ChromeController",

	#
	# license="LICENSE.txt",
	description="Chrome Remote Debugger interface.",

	long_description=open("README.md").read(),

	dependency_links=[
		'https://github.com/berkerpeksag/astor/tarball/master#egg=astor-0.6',
	],

	# Dependent packages (distributions)
	install_requires=[
		'websocket-client',
		'astor>=0.6',
		'requests',
		'cachetools',
		'webrequest',
	],
)
