# Copyright (C) 2012 Benjamin Althues
#
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
#
# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

from django.template import Library, Node, TemplateSyntaxError

from navigation.sections import Sections

register = Library()

class MenuNode(Node):
    def __init__(self, section):
        self.retstr = ''

        nItems = len(Sections.items)
        i = 1

        for item in Sections.order:
            if item == section:
                self.retstr += '%s' % item.capitalize()
            else:
                self.retstr += '<a href="%s">%s</a>' % (
                        Sections.items[item], item.capitalize())

            if i != nItems:
                self.retstr += ' | '
                i += 1

    def render(self, context):
        return self.retstr

@register.tag
def menu(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("'menu' statement takes one argument")

    return MenuNode(bits[1])
