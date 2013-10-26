#!/usr/bin/env python3
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from subprocess import Popen, PIPE
import os

'''
	(c) 2012 Christoph Grenz <christophg@grenz-bonn.de>
	This file is part of python-osm.

	python-hiddev is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	python-osm is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with python-osm.  If not, see <http://www.gnu.org/licenses/>.
'''

setup(
  name = 'HIDDev',
  packages = ['hiddev'],
  scripts = ['hiddevexplorer']
)
