# coding=utf-8
from bbb import getSite
from collective.recaptcha import RecaptchaMessageFactory as _
from persistent import Persistent
from plone.registry.interfaces import IRegistry
from zope import schema
from zope.annotation import factory
from zope.annotation import IAttributeAnnotatable
from zope.component import adapts
from zope.component import getUtility
from zope.interface import implements
from zope.interface import Interface


try:
    from zope.formlib.form import FormFields
except ImportError:
    # formlib missing (Plone 5?)
    FormFields = None


try:
    # formlib missing (Plone 5?)
    from plone.app.registry.browser.controlpanel import RegistryEditForm as EditForm  # noqa
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

    public_key = schema.TextLine(
        title=_(u'Public Key')
    )

    private_key = schema.TextLine(
        title=_(u'Private Key')
    )

    multilingual = schema.Bool(
        title=_(u'Multilingual'),
        description=_(u"Check field to use portal's language."),
        default=True,
        required=False
    )

    default_language = schema.Choice(
        title=_(u'Default Language'),
        description=_(u'Uncheck multilingual field to use the language below.'),
        vocabulary="collective.recaptcha.settings.AvailableLanguages",
        default="en",
    )

    default_theme = schema.Choice(
        title=_(u'Default Theme'),
        vocabulary="collective.recaptcha.settings.AvailableThemes",
        default="light"
    )

    fallback = schema.Bool(
        title=_(u'Fallback'),
        description=_(u"Check field to use fallback version of recaptcha."),
        default=False,
        required=False
    )


class RecaptchaSettingsAnnotations(Persistent):
    implements(IRecaptchaSettings)
    adapts(IAttributeAnnotatable)

    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.multilingual = True
        self.default_language = 'en'
        self.default_theme = 'light'
        self.fallback = False

RecaptchaSettings = factory(RecaptchaSettingsAnnotations)


def getRecaptchaSettings():
    registry = getUtility(IRegistry)
    if TRY_REGISTRY:
        # if plone.formwidget.recaptcha is installed, try getting
        # its settings from the registry
        try:
            settings = registry.forInterface(IReCaptchaSettings)
            if settings.public_key and settings.private_key \
                    and settings.multilingual and settings.default_language\
                    and settings.default_theme and settings.fallback:
                return settings
        except:
            pass
    # try getting settings from the registry first
    try:
        settings = registry.forInterface(IRecaptchaSettings)
        if settings.public_key and settings.private_key \
                and settings.multilingual and settings.default_language \
                and settings.default_theme and settings.fallback:
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
