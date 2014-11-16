#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/cyrus.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Cyrus Mailserver fabric commands

"""

import fabrications.cyrus_helper as helper

def create_mailbox(mailbox_user):
    """CYRUS: Create a new mailbox for the specified user."""

    configuration = helper.get_config()
    connection = helper.login(configuration["hostname"],
        configuration["username"],
        configuration["password"])
    try:
        connection.create("user." + mailbox_user)
        # this crazy syntax is required otherwise the module just gives errors
        connection.setquota("user." + mailbox_user,
            "(storage %s)" % configuration["default_quota"])
    finally:
        connection.logout()



