#!/usr/bin/env python2
import web
from web import form

render = web.template.render('tpl/', base='base')
urls = (
    '/',            'index',
    '/dispass/',    'dispass',
    '/rot13/',      'rot13',
    '/springwhiz/', 'springwhiz',
)
app = web.application(urls, globals())

rot13_form = form.Form(form.Textarea('text'))


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
