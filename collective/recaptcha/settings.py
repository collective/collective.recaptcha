from persistent import Persistent
from zope.interface import Interface, implements
from zope.component import adapts
from zope.app.component.hooks import getSite
from zope import schema
from zope.annotation import factory, IAttributeAnnotatable

try:
    from Products.Five.formlib.formbase import EditForm
except ImportError:
    from zope.formlib.form import EditForm
from zope.formlib.form import FormFields

from collective.recaptcha import RecaptchaMessageFactory as _

class IRecaptchaSettings(Interface):
    
    public_key = schema.TextLine(
        title = _(u'Public Key')
        )
        
    private_key = schema.TextLine(
        title = _(u'Private Key')
        )

class RecaptchaSettingsAnnotations(Persistent):
    implements(IRecaptchaSettings)
    adapts(IAttributeAnnotatable)

    def __init__(self):
        self.public_key = None
        self.private_key = None
RecaptchaSettings = factory(RecaptchaSettingsAnnotations)

def getRecaptchaSettings():
    site = getSite()
    return IRecaptchaSettings(site)

class RecaptchaSettingsForm(EditForm):
    form_fields = FormFields(IRecaptchaSettings)
    label = _(u"Recaptcha settings")
