#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 16:45:15 EST 2013
# 
# 

"""
    Simply contains a list of all the package containers that will be
    installed
"""

import haskell_packs
import j_packs
import latex_packs
import miscmath_packs
import office_packs
import python_packs
import r_packs

# Add or remove containers of packages here, make sure they
# are imported above!
package_containers = [haskell_packs.container,
                      j_packs.container,
                      latex_packs.container,
                      miscmath_packs.container,
                      office_packs.container,
                      python_packs.container,
                      r_packs.container]
