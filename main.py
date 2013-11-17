# Copyright (c) 2013  Benjamin Althues <benjamin@babab.nl>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import sys
import web
from web import form

from string_generator import stringGenerator

version = '6.0.1'
urls = (
    '/',            'index',
    '/dispass/',    'dispass',
    '/rot13/',      'rot13',
    '/springwhiz/', 'springwhiz',
    '/strgen/',     'strgen',
)

rot13_form = form.Form(form.Textarea('text'))
strgen_form = form.Form(
    form.Textbox("nchars",
                 form.notnull,
                 form.regexp('\d+', 'Must be a digit'),
                 form.Validator('Must be more then 0 and less then 109',
                                lambda x: int(x) > 0 and int(x) < 109),
                 class_='span1', value=50, description='Number of chars'),
    form.Checkbox('range1', value=1, description='Range a-z', checked=True),
    form.Checkbox('range2', value=2, description='Range A-Z', checked=True),
    form.Checkbox('range3', value=3, description='Range 0-9', checked=True),
    form.Checkbox('range4', value=4, description='Special chars',
                  checked=True),
    form.Checkbox('range5', value=5, description='Include !,1,l,i,I,0,o,O'),
)

render = web.template.render(
    'tpl/', base='base',
    globals={'getattr': getattr,
             'version_babab': version,
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
        form = strgen_form()
        return render.strgen(form, False)

    def POST(self):
        form = strgen_form()
        if form.validates():
            charOptions = []
            for ri in range(1, 6):
                if getattr(form.d, 'range%s' % ri):
                    charOptions.append(ri)

            result = stringGenerator(charOptions, int(form.d.nchars))
            return render.strgen(form, result)
        else:
            return render.strgen(form, False)
