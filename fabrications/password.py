#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Password related fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import run, task
from os.path import basename, splitext
import configuration as config

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
def change_password(password_type):
    """(PASSWORD) Change password. | (string) password_type."""

    if password_type == "local":
        run("passwd")
