#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
feedback.py (library)

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Provide feedback to the user on stdout.

"""

SCRIPTNAME = "UNINITIALIZED"

def register(name):
    """Register the name of the script which wants to provide feedback."""
    global SCRIPTNAME
    SCRIPTNAME = name

def give(message):
    """Print a message to stdout, prefixed with the name of the script"""
    print SCRIPTNAME + ": " + message
