#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Postfix fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

import configuration as config
from fabric.api import task, run
from os.path import splitext, basename

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
def renew_aliases():
    """(POSTFIX): Read in the aliases file."""

    command = "newaliases"
    run(command)
