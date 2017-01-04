import os
from sphinx.domains import python as pdom

__version__ = "0.1.0"


class GAttributePyClassmember(pdom.PyClassmember):
    def get_signature_prefix(self, sig):
        return u'\u2666 '


pdom.PythonDomain.object_types['gattribute'] = pdom.ObjType(
    pdom.l_('gattribute'), 'gattr', 'obj')
pdom.PythonDomain.directives['gattribute'] = GAttributePyClassmember
pdom.PythonDomain.roles['gattr'] = pdom.PyXRefRole()


def get_html_theme_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), 'themes'))
