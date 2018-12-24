from setuptools import setup, find_packages
from codecs import open
from os import path


dir_path = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(dir_path, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
	name='Image-Filters',
	version = '1.0',
	author= 'Ishita Das',
	author_email= '',
	url= 'https://github.com/ishita27/Image-Filters',
	description = "This project aims towards making Image filters using the python OpenCV library \nthat can be used as filters for an photo editing application.",
	long_description = long_description,
#Listing Dependencies that it has
	install_requires = requirements,
#LICENSE Info
	license= 'The MIT License 2018',
#INFO about where package can run
	classifiers=[
	'Intended Audience :: Developers',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Operating System :: Windows',
	'Operating System :: Linux',
	]
)
