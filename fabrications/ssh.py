#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/ssh.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

SSH fabric commands

"""

from fabric.api import run, settings, hide, env, task
import re

@task
def get_fingerprints():
    """SSH: Retrieve a machine's fingerprints"""

    ssh_key_locations = ["ssh_host_dsa_key",
        "ssh_host_key",
        "ssh_host_rsa_key",
        "ssh_host_ecdsa_key",
        ]

    retrieved_keys = []

    with settings(warn_only=True), hide("stdout", "warnings"):
        for key in ssh_key_locations:
            full_key = "/etc/ssh/" + key + ".pub"
            found_key = run("ssh-keygen -l -f " + full_key)
            if found_key is not None:
                if re.match("[0-9]", found_key[0]) is not None:
                    retrieved_keys.append(found_key)


    print "\n"
    print "Fingerprints for " + env.host
    for key in retrieved_keys:
        print key
    print "\n"
