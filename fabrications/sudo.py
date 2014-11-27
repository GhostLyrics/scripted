#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sudo fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

import configuration as config
from fabric.api import task
from fabric.contrib.files import append
from os.path import splitext, basename

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################

@task
def allow_passwordless_sudo(username):
    """(SUDO) Enable a user to use sudo without password."""

    sudo_string = "{} ALL=(ALL) NOPASSWD: ALL\n".format(username)
    append("/etc/sudoers", sudo_string, use_sudo=True)
