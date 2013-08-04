#!/usr/bin/env python2
import web
from main import app

web.config.debug = False
web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
app.run()
