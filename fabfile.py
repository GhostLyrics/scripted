#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Collects all fabrications.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import env
env.use_ssh_config = True

from fabrications.cron import *
from fabrications.cyrus import *
from fabrications.dhcp import *
from fabrications.networking import *
from fabrications.ssh import *
