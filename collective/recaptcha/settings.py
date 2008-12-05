from persistent import Persistent
from zope.interface import Interface, implements
from zope.component import adapts
from zope.app.component.hooks import getSite
from zope import schema
from zope.annotation import factory, IAttributeAnnotatable

# XXX i18n

class IRecaptchaSettings(Interface):
    
    public_key = schema.TextLine(
        title = u'Public Key'
        )
        
    private_key = schema.TextLine(
        title = u'Private Key'
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
