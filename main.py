#!/usr/bin/env python2
import sys
import web
from web import form

version = '6.0.0-dev'
urls = (
    '/',            'index',
    '/dispass/',    'dispass',
    '/rot13/',      'rot13',
    '/springwhiz/', 'springwhiz',
)

rot13_form = form.Form(form.Textarea('text'))

render = web.template.render(
    'tpl/', base='base',
    globals={'version_babab': version,
             'version_python': sys.version.split()[0],
             'version_webpy': web.__version__}
)
app = web.application(urls, globals())


class index:
    def GET(self):
        return render.index()


class dispass:
    def GET(self):
        return render.dispass()


class springwhiz:
    def GET(self):
        return render.springwhiz()


class rot13:
    def GET(self):
        form = rot13_form()
        return render.rot13(form)

    def POST(self):
        form = rot13_form()
        if form.validates():
            return render.rot13(form)
        else:
            return 'Invalid entry'


class strgen:
    def GET(self):
        return render.strgen()

if __name__ == '__main__':
    app.run()
