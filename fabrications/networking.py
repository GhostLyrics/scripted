#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Network fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import run, hide, env, task
from os.path import splitext, basename
import fabrications.configuration as config
import re


# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
def get_IPs():  # pylint: disable=C0103
    """(NETWORK) Retrieve IP, network interface & MAC address of a machine."""

    information = None
    with hide("stdout"):
        information = run("ifconfig")

    lines = information.split("\n")
    count = 0

    print "\n"
    print "IP information for " + env.host

    for line in lines:
        if re.match("eth", line) is not None:

            interface = lines[count].split()[0]
            mac_address = lines[count].split()[4]

            # r: raw string
            # [0-9]+: one or more digits
            # \.: escape dot so it is not treated as regex syntax
            regex = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
            try:
                ip_address = re.findall(regex, lines[count+1])[0]
            except IndexError:
                print "Interface is up but has no IP."
            else:
                print "IP: " + ip_address,
                print " on " + interface,
                print " with MAC " + mac_address

        count = count + 1
    print "\n"
