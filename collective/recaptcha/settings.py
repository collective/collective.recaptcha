from persistent import Persistent
from zope.interface import Interface, implements
from zope.component import adapts, getUtility
from zope.app.component.hooks import getSite
from zope import schema
from zope.annotation import factory, IAttributeAnnotatable

try:
    from Products.Five.formlib.formbase import EditForm
except ImportError:
    from zope.formlib.form import EditForm
from zope.formlib.form import FormFields

try:
    from plone.registry.interfaces import IRegistry
    from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
    TRY_REGISTRY = True
except ImportError:
    TRY_REGISTRY = False

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
    if TRY_REGISTRY:
        # if plone.formwidget.recaptcha is installed, try getting
        # its settings from the registry
        try:
            registry = getUtility(IRegistry)
            settings = registry.forInterface(IReCaptchaSettings)
            if settings.public_key and settings.private_key:
                return settings
        except:
            pass

    # if its not installed, or the settings haven't been configured,
    # fall back to our storage of an annotation on the site
    site = getSite()
    return IRecaptchaSettings(site)


class RecaptchaSettingsForm(EditForm):
    form_fields = FormFields(IRecaptchaSettings)
    label = _(u"Recaptcha settings")
