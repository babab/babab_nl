from django import get_version as django_version
from sys import version as python_version

from settings import BABAB_VERSION as babab_version

def platform_version_info(request):
    return { 'version_babab': babab_version,
             'version_python': python_version.split()[0],
             'version_django': django_version() }
