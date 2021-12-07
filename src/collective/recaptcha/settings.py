# coding=utf-8
from bbb import getSite
from collective.recaptcha import RecaptchaMessageFactory as _
from persistent import Persistent
from plone.registry.interfaces import IRegistry
from zope import schema
from zope.annotation import factory
from zope.annotation import IAttributeAnnotatable
from zope.component import adapter
from zope.component import getUtility
from zope.interface import implementer
from zope.interface import Interface


try:
    from zope.formlib.form import FormFields
except ImportError:
    # formlib missing (Plone 5?)
    FormFields = None


try:
    # formlib missing (Plone 5?)
    from plone.app.registry.browser.controlpanel import RegistryEditForm as EditForm
except ImportError:
    try:
        # Zope 2.12+
        from five.formlib.formbase import EditForm
    except ImportError:
        try:
            # older Zope 2s
            from Products.Five.formlib.formbase import EditForm
        except ImportError:
            # Zope 3
            from zope.formlib.form import EditForm

try:
    from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings

    TRY_REGISTRY = True
except ImportError:
    TRY_REGISTRY = False


class IRecaptchaSettings(Interface):

    public_key = schema.TextLine(title=_(u"Site Key"))

    private_key = schema.TextLine(title=_(u"Secret Key"))


@implementer(IRecaptchaSettings)
@adapter(IAttributeAnnotatable)
class RecaptchaSettingsAnnotations(Persistent):
    def __init__(self):
        self.public_key = None
        self.private_key = None


RecaptchaSettings = factory(RecaptchaSettingsAnnotations)


def getRecaptchaSettings():
    registry = getUtility(IRegistry)
    if TRY_REGISTRY:
        # if plone.formwidget.recaptcha is installed, try getting
        # its settings from the registry
        try:
            settings = registry.forInterface(IReCaptchaSettings)
            if settings.public_key and settings.private_key:
                return settings
        except (AttributeError, KeyError):
            pass
    # try getting settings from the registry first
    try:
        settings = registry.forInterface(IRecaptchaSettings)
        if settings.public_key and settings.private_key:
            return settings
    except KeyError:
        # fall back to our storage of an annotation on the site if the settings
        # haven't been configured
        site = getSite()
        return IRecaptchaSettings(site)


class RecaptchaSettingsForm(EditForm):
    schema = IRecaptchaSettings
    label = _(u"Recaptcha settings")

    if FormFields:
        # formlib missing (Plone 5?)
        form_fields = FormFields(IRecaptchaSettings)
