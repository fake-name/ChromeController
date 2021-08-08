
import setuptools
from distutils.core import setup
import sys
import time

win_req = ["pywin32"] if sys.platform.startswith("win") else []

setup(
	# Application name:
	name="ChromeController",

	# Version number (initial):
	version="0.3.25",

	# Application author details:
	author="Connor Wolf",
	author_email="github@imaginaryindustries.com",

	# Packages
	packages=setuptools.find_packages(),
	package_dir = {'ChromeController': 'ChromeController'},

	# Bundle the protocol json files.
	package_data={
		'ChromeController': [
			'protocols/*.json',
			'resources/evasions/*.js'
		]},

	# Details
	url="https://github.com/fake-name/ChromeController",

	#
	# license="LICENSE.txt",
	description="Chrome Remote Debugger interface.",

	long_description=open("README.md").read(),
	long_description_content_type = "text/markdown",

	# dependency_links=[
	# 	'https://github.com/berkerpeksag/astor/tarball/master#egg=astor-0.6',
	# ],

	# Dependent packages (distributions)
	install_requires=[
		'websocket-client',
		'astor>=0.6',
		'requests',
		'cachetools',
		'docopt',
	# We need pywin32 on windows for proper process termination.
	] + win_req,

	classifiers                   = [
		"Programming Language :: Python :: 3",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Operating System :: POSIX :: Linux",
	],

)
