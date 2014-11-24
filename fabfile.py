#!/usr/bin/env python
# -*- coding: utf-8 -*-

# disabling due to recommended usage of fabric API
# pylint: disable=wildcard-import, unused-wildcard-import

"""
fabfile.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Collects all fabrications.

"""

from fabric.api import env
env.use_ssh_config = True

from fabrications.cron import *
from fabrications.cyrus import *
from fabrications.dhcp import *
from fabrications.networking import *
from fabrications.ssh import *
