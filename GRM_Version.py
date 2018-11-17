#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 22:04:18 2018

Miscellanous functions for GREMLIB module.

@author: echambon
"""

VERSION_MAJOR = 0
VERSION_MINOR = 0

def get_version_major():
    return VERSION_MAJOR

def get_version_minor():
    return VERSION_MINOR

def print_version():
    print(str(VERSION_MAJOR)+'.'+str(VERSION_MINOR))