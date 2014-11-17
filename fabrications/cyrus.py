#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/cyrus.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Cyrus Mailserver fabric commands

"""

from fabric.api import task

import json
import os
import imaplib

# tasks

@task
def create_mailbox(mailbox_user):
    """CYRUS: Create a new mailbox for the specified user."""

    configuration = get_config()
    connection = login(configuration["hostname"],
        configuration["username"],
        configuration["password"])
    try:
        connection.create("user." + mailbox_user)
        # this crazy syntax is required otherwise the module just gives errors
        connection.setquota("user." + mailbox_user,
            "(storage %s)" % configuration["default_quota"])
    finally:
        connection.logout()


# internal functions

def login(server, username, password):
    """Authenticate to the IMAP server"""

    connection = imaplib.IMAP4_SSL(server)
    connection.login(username, password)
    return connection

def get_config():
    """Read the configuration from configuration/cyrus.json"""

    fabric_path = os.path.dirname(os.path.realpath(__file__))
    prefix = os.path.dirname(fabric_path)
    configuration_path = os.path.join(prefix, "configuration/cyrus.json")

    with open(configuration_path) as configuration:
        return json.load(configuration)
