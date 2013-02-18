#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Fri Jan 25 17:20:17 EST 2013
# 
# 

"""
    The Ultimate Dev. Machine script. Run with sudo to turn a virtual
    machine into a developer's heaven.
"""

import packs
from os import system
from datetime import datetime

def install_desired_packs(successful_packs):
    """
        Loops through the desired containers and installs them
    """

    failed_packs = []

    for container in packs.desired_packages.package_containers:
        failed_packs += container.install_me(successful_packs)

    if failed_packs != []:
        print "\nThe following packages failed to install correctly:"
        print "\n".join(pack_name for pack_name in failed_packs)
    else:
        print "\nEverything installed correctly"

def get_string_name_and_pack(name, pack):
    """
        Returns a string like "<Software Name> (<Package Name>)"
        where (<Package Name>) can be empty if none exists.
    """
    return name + (' (' + pack + ')' if pack != None else '') + '\n'

def get_string_of_packages():
    """
        Returns a string of all packages that ought to be
        installed
    """
    packages = ''
    for container in packs.desired_packages.package_containers:
        packages += get_string_name_and_pack(container.name, container.package)
        for name in container.packages:
            packages += '-> ' + get_string_name_and_pack(name,
                                                        container.packages[name])
        if container.special_instructions:
            for name in container.special_instructions:
                packages += '-> ' + get_string_name_and_pack(name, None)
    return packages

def write_dict_as_html(dic, file_name):
    """
        A quickly built function to make an html log
    """
    now = str(datetime.now())

    f = open(file_name, 'w')
    f.write('<html>\n  <head>\n  </head>\n  <body>\n')
    f.write('    <h2>Ultimate Math Machine</h2>')
    f.write('    <h3>Installation on: %s</h3>' % now)
    for container in dic:
        f.write('    <h5>%s<h5>\n    <ol>\n' % container) 
        for package in dic[container]: 
            f.write('      <li>%s</li>\n' % package)
        f.write('    </ol><br />\n\n')
    f.write('  </body>\n</html>')
     

def prompter():
    """
        Asks the user whether they want to install the software
        or not
    """
    
    system('echo "' + get_string_of_packages() +'" | less')

    return raw_input("Install the listed software? (yes/no): ").lower().startswith('y')

if __name__ == '__main__':
    system('apt-get update')
    log_name = "umm_log.html"
    successful_packs = {}
    if prompter():
        install_desired_packs(successful_packs)
    write_dict_as_html(successful_packs, log_name)
    system('firefox ' + log_name)
