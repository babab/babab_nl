#!/usr/bin/python
import sys, os
from django.core.servers.fastcgi import runfastcgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'babab_nl.settings'
runfastcgi(method='threaded', daemonize='false',
           pidfile='/tmp/django-babab_nl.pid')
