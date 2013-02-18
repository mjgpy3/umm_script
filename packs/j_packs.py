#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:47:44 EST 2013
# 
# 

from package_container import PackageContainer

packages = {}

special_package_instructions = {'J': 
                                    ['wget http://www.jsoftware.com/download/j701a_linux32.sh',
                                     'sh j701a_linux32.sh -install',
                                     'rm j701a_linux32.sh']}

container = PackageContainer("J", None, packages, special_package_instructions)
