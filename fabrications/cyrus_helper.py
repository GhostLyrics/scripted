#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/cyrus_helper.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Cyrus helper: hides internal complexity and commands from fabric

"""

import imaplib
import json

def login(server, username, password):
    """Authenticate to the IMAP server"""

    connection = imaplib.IMAP4_SSL(server)
    connection.login(username, password)
    return connection

def get_config():
    """Read the configuration from /configuration/cyrus.json"""

    with open("./configuration/cyrus.json") as configuration:
        return json.load(configuration)
