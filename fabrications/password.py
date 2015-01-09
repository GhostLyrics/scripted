#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Password related fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import run, task
from os.path import basename, splitext
import fabrications.configuration as config

# module configuration ########################################################


MODULE = splitext(basename(__file__))[0]
CONFIGURATION = config.get_configuration(MODULE)


# tasks #######################################################################


@task
def change_password(password_type, username="self"):
    """(PASSWORD) Change password. | (string) password_type, (string) user.

    Arguments:
        password_type can be either 'local' or 'samba'
        user will default to the user you log in with if unspecified

    """

    if password_type == "local":
        command = "passwd"
    elif password_type == "samba":
        command = "smbpasswd"

    if username != "self":
        command = "{} {}".format(command, username)

    run(command)
