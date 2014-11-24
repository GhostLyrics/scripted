#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/configuration.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Configuration module for other fabrications

"""

import json
import os

# module configuration ########################################################

FABRIC_PATH = os.path.dirname(os.path.realpath(__file__))
PREFIX = os.path.join(os.path.dirname(FABRIC_PATH), "configuration")

# internal functions ##########################################################

def get_configuration(module):
    """Read the configuration from configuration/cyrus.json"""

    configuration_path = os.path.join(PREFIX, "{}.json".format(module))
    try:
        with open(configuration_path) as configuration:
            return json.load(configuration)
    except IOError:
        print "No configuration file for module {}".format(module)
