from zope.interface import implements
from zope.schema import ASCIILine
from zope.schema.interfaces import IASCIILine
from zope.component._api import getMultiAdapter
from zope.app.form.interfaces import ConversionError

from Acquisition import aq_inner

class ICaptcha(IASCIILine):
    """A field for captcha validation"""


class Captcha(ASCIILine):
    implements(ICaptcha)


