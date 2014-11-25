#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cyrus Mailserver fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

import imaplib
import fabrications.configuration as config
from fabric.api import task, run, hosts
from os.path import splitext, basename

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# internal functions ##########################################################


def login(server, username, password):
    """Authenticate to the IMAP server."""
    connection = imaplib.IMAP4_SSL(server)
    connection.login(username, password)
    return connection


# tasks #######################################################################


@task
def create_mailbox(mailbox_user):
    """(CYRUS) Create a new mailbox for the specified user."""
    connection = login(CONFIGURATION["hostname"],
                       CONFIGURATION["username"],
                       CONFIGURATION["password"])
    try:
        connection.create("user." + mailbox_user)

        # this crazy syntax is required otherwise the module just gives errors
        connection.setquota(
            "user.{}".format(mailbox_user),
            "(storage {})".format(CONFIGURATION["default_quota"])

    finally:
        connection.logout()


@task
@hosts(CONFIGURATION["hostname"])
def connect_cyrus():
    """(CYRUS) Open the cyrus 'cyradm' shell."""

    user = CONFIGURATION["username"]
    command = "cyradm --user {} --authz {} localhost".format(user, user)
    run(command)
