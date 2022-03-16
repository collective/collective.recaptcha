# coding=utf-8
from collective.recaptcha import RecaptchaMessageFactory as _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.registry.interfaces import IRegistry
from zope import schema
from zope.component import getUtility
from zope.interface import Interface


try:
    from plone.formwidget.recaptcha.interfaces import IReCaptchaSettings

    TRY_FORMWIDGET = True
except ImportError:
    TRY_FORMWIDGET = False


class IRecaptchaSettings(Interface):

    public_key = schema.TextLine(title=_(u"Site Key"))

    private_key = schema.TextLine(title=_(u"Secret Key"))


def getRecaptchaSettings():
    registry = getUtility(IRegistry)
    if TRY_FORMWIDGET:
        # if plone.formwidget.recaptcha is installed, try getting
        # its settings from the registry
        try:
            settings = registry.forInterface(IReCaptchaSettings)
            if settings.public_key and settings.private_key:
                return settings
        except (AttributeError, KeyError):
            pass
    settings = registry.forInterface(IRecaptchaSettings)
    if settings.public_key and settings.private_key:
        return settings


class RecaptchaSettingsForm(RegistryEditForm):
    schema = IRecaptchaSettings
    label = _(u"Recaptcha settings")
