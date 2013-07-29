#!/usr/bin/env python2
import web

render = web.template.render('tpl/', base='base')
urls = (
    '/',            'index',
    '/dispass/',    'dispass',
    '/springwhiz/', 'springwhiz',
)


class index:
    def GET(self):
        return render.index()


class dispass:
    def GET(self):
        return render.dispass()


class springwhiz:
    def GET(self):
        return render.springwhiz()

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
