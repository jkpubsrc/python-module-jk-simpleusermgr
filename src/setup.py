################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module implements a very simple user manager. Such a simple user manager is convenient in a variety of situations for small applications.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-simpleusermgr/tarball/0.2020.4.16",
	include_package_data = False,
	install_requires = [
		"jk_utils",
	],
	keywords = [
		"user",
	],
	license = "Apache 2.0",
	name = "jk_simpleusermgr",
	packages = [
		"jk_simpleusermgr",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-simpleusermgr",
	version = "0.2020.4.16",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
