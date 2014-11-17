#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fabrications/cron.py

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

Cronjob fabric commands

"""

from fabric.api import run, settings, hide, env, task

@task
def get_cronjobs():
    """CRON: Retrieve lists of custom and scheduled cronjobs"""

    with settings(warn_only=True), hide("stdout", "warnings"):
        crontab = run("crontab -l")
        etc_cronjobs = run("ls /etc/cron.*")
        cronfile = run("cat /etc/crontab | grep ^[0-9]")

    print "\n"
    print "Cronjobs for " + env.host

    print "Content of crontab: "
    print crontab + "\n"

    print "Scheduled cronjobs: "
    print etc_cronjobs + "\n"

    print "Jobs in custom cronfile: "
    print cronfile + "\n"
