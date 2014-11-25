#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cronjob fabric commands.

:copyright: (c) 2014 by Alexander Skiba <skiba@icg.tugraz.at>
:licence: MIT
:bugreports: skiba@icg.tugraz.at

"""

from fabric.api import run, settings, hide, env, task


# tasks #######################################################################


@task
def get_cronjobs():
    """(CRON) Retrieve lists of custom and scheduled cronjobs."""
    with settings(warn_only=True), hide("stdout", "warnings"):
        crontab = run("crontab -l")
        etc_cronjobs = run("ls /etc/cron.*")
        cronfile = run("cat /etc/crontab | grep ^[0-9]")

    print "\nCronjobs for {}".format(env.host)
    print "Content of crontab: {}\n".format(crontab)
    print "Scheduled cronjobs: {}\n".format(etc_cronjobs)
    print "Jobs in custom cronfile: {}\n".format(cronfile)
