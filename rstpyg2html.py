try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.parsers.rst import directives
import rst2pdf.pygments_code_block_directive

directives.register_directive(
    'code-block',
    rst2pdf.pygments_code_block_directive.code_block_directive
)

description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)
publish_cmdline(writer_name='html', description=description)
