# -*- coding: utf-8 -*-

import locale
import os

from fabric.api import *

locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
local_path = os.path.dirname(os.path.abspath(__file__))

env.use_ssh_config = True


def hello():
    print("Hello world!")


def restart_nginx(host, user='admin'):
    with settings(host_string=host, user=user):
        run("sudo service nginx restart")


def restart_supervisor(host, user='admin'):
    with settings(host_string=host, user=user):
        run("sudo service supervisor restart")


def restart_gunicorn(host, user='admin'):
    with settings(host_string=host, user=user):
        run("sudo supervisorctl restart mapa-de-medios")


def deploy(host, branch, user='admin'):
    print "Pull in host: %s, branch: %s" % (host, branch)
    with settings(host_string=host, user=user):
        run("cd /home/admin/html/mapa-de-medios; git pull origin %s" % branch)


def deploy_staging():
    host = 'staging.poderopedia.org'
    branch = 'staging'
    deploy(host, branch)


def deploy_dev():
    host = 'dev.poderopedia.org'
    branch = 'dev'
    deploy(host, branch)


def deploy_production():
    host = 'www.poderopedia.org'
    branch = 'master'
    deploy(host, branch)


def deploy_prod():
    deploy_production()
