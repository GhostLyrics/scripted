#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
system.py (library)

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Detect the used system and distribution to warn on incompatible systems.

"""

import platform
import library.feedback as feedback

def get_system():
    """Returns the system name or if on linux, the short distribution name."""
    system = platform.system()

    if system == "Linux":
        # rewrite system to be the short distribution name if on linux
        system = platform.linux_distribution()[0]

    return system

def compatible(compatible_systems):
    """Checks if the script in question is compatible with the system."""
    if get_system() in compatible_systems:
        feedback.give("System compatible.")
    else:
        feedback.give("System not compatible.")
        feedback.give("Compatible systems are: {}".format(compatible_systems))
        exit(1)

