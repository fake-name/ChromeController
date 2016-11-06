
import setuptools
from distutils.core import setup
import sys
setup(
	# Application name:
	name="ChromeController",

	# Version number (initial):
	version="0.0.1",

	# Application author details:
	author="Connor Wolf	",
	author_email="github@imaginaryindustries.com",

	# Packages
	packages=["ChromeController"],

	# Details
	url="https://github.com/fake-name/ChromeController",

	#
	# license="LICENSE.txt",
	description="Chrome Remote Debugger interface.",

	long_description=open("README.md").read(),

	# Dependent packages (distributions)
	install_requires=[
	],
)
