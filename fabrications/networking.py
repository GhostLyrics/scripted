#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/networking.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Network related fabric commands

"""

from fabric.api import run, hide
import re

def get_IPs():
    """NETWORK: Retrieve IP, network interface and MAC address of a machine."""

    information = None
    with hide("stdout"):
        information = run("ifconfig")

    lines = information.split("\n")
    count = 0
    for line in lines:
        if re.match("eth", line) is not None:

            interface = lines[count].split()[0]
            mac_address = lines[count].split()[4]

            # r: raw string
            # [0-9]+: one or more digits
            # \.: escape dot so it is not treated as regex syntax
            regex = r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
            ip_address = re.findall(regex, lines[count+1])[0]

            print "IP: " + ip_address,
            print " on " + interface,
            print " with MAC " + mac_address

        count = count + 1
