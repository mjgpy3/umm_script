#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Thu Jan 31 16:06:58 EST 2013
# 
# 

"""
    A hacked together tool for making commits easier
"""

from os import system

clean = lambda: system('find .. -name "*.pyc" | xargs rm')

if __name__ == '__main__':
    clean()

    # No error has occured
    if system('pychecker ../umm.py') == 0:
        system('git add ..')
        system('git commit -m "' + raw_input('Commit Message: \n')  +'"')
        system('git push')
    else:
        print "There is an error in the code!!!"
        print "Debug, monkey! Debug!!!"

    clean()
