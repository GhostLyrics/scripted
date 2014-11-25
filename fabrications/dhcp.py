#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DHCP Server fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

import configuration as config
from fabric.api import task, run, hosts
from os.path import splitext, basename


# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
@hosts(CONFIGURATION["hostname"])
def restart_dhcp():
    """(DHCP) Restart the DHCP service."""
    run("service isc-dhcp-server restart")
