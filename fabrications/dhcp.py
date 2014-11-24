#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/dhcp.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

DHCP Server fabric commands

"""


from fabric.api import task, run, hosts
from os.path import splitext, basename
import fabrications.configuration as config

# module configuration ########################################################

MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)

# tasks #######################################################################

@task
@hosts(CONFIGURATION["hostname"])
def restart_dhcp():
    """DHCP: Restart the DHCP service"""
    run("service isc-dhcp-server restart")
