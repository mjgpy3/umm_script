#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {'Sympy': 'python-sympy', 
            'Numpy': 'python-numpy',
            'Scipy': 'python-scipy',
            'Matplotlib': 'python-matplotlib',
            'Spyder': 'spyder'}

container = PackageContainer("Python", 'python', packages)
