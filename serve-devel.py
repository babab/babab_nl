#!/usr/bin/env python2
import web
from main import app

web.config.debug = True
app.run()
