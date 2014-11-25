#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Password related fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import run, task

# tasks #######################################################################


@task
def change_password(password_type):
    """(PASSWORD) Change password. | Arguments: (string) password_type."""

    if password_type == "local":
        run("passwd")
