#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Homebrew package manager for OS X fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

import fabrications.configuration as config
from os.path import splitext, basename
from fabric.api import run, task

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
def brew_upgrade():
    """(HOMEBREW) Update formulas and upgrade installed formulas."""

    update_command = "brew update"
    upgrade_command = "brew upgrade"

    run(update_command)
    run(upgrade_command)
