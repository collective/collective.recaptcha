# -*- coding: utf8 -*-
from persistent import Persistent
from zope.interface import Interface, implements
from zope.component import adapts
from zope.component import getUtility
from zope import schema
from zope.annotation import factory, IAttributeAnnotatable
from bbb import getSite

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

from zope.formlib.form import FormFields


try:
    from plone.registry.interfaces import IRegistry
    HAS_REGISTRY = True
except ImportError:
    HAS_REGISTRY = False

if HAS_REGISTRY:
    try:
        from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings
        TRY_REGISTRY = True
    except ImportError:
        TRY_REGISTRY = False
else:
    TRY_REGISTRY = False

from collective.recaptcha import RecaptchaMessageFactory as _


class IRecaptchaSettings(Interface):

    public_key = schema.TextLine(
        title=_(u'Public Key')
    )

    private_key = schema.TextLine(
        title=_(u'Private Key')
    )


class RecaptchaSettingsAnnotations(Persistent):
    implements(IRecaptchaSettings)
    adapts(IAttributeAnnotatable)

    def __init__(self):
        self.public_key = None
        self.private_key = None

RecaptchaSettings = factory(RecaptchaSettingsAnnotations)


def getRecaptchaSettings():
    # If we do not have registry do not even try to use it
    if not HAS_REGISTRY:
        site = getSite()
        return IRecaptchaSettings(site)

    registry = getUtility(IRegistry)
    if TRY_REGISTRY:
        # if plone.formwidget.recaptcha is installed, try getting
        # its settings from the registry
        try:
            settings = registry.forInterface(IReCaptchaSettings)
            if settings.public_key and settings.private_key:
                return settings
        except:
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
    form_fields = FormFields(IRecaptchaSettings)
    label = _(u"Recaptcha settings")
