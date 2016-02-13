from django import template

from bababblog.lib import str2hex

register = template.Library()


@register.filter
def hex(value):
    return str2hex(value)
