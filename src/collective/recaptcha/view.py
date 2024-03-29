# coding=utf-8
from collective.recaptcha import RecaptchaMessageFactory as _
from collective.recaptcha.settings import getRecaptchaSettings
from norecaptcha.captcha import displayhtml
from norecaptcha.captcha import submit
from Products.Five import BrowserView
from zope import schema
from zope.annotation import factory
from zope.component import adapter
from zope.component import queryMultiAdapter
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserRequest


class IRecaptchaInfo(Interface):
    error = schema.TextLine()
    verified = schema.Bool()


@implementer(IRecaptchaInfo)
@adapter(IBrowserRequest)
class RecaptchaInfoAnnotation(object):
    def __init__(self):
        self.error = None
        self.verified = False


RecaptchaInfo = factory(RecaptchaInfoAnnotation)


class RecaptchaView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.settings = getRecaptchaSettings()

    def image_tag(self):
        portal_state = queryMultiAdapter(
            (self.context, self.request), name=u"plone_portal_state"
        )
        lang = portal_state.language()[:2]

        if not self.settings.public_key:
            raise ValueError(
                _(u"No recaptcha public key configured. ")
                + _(u"Go to /@@recaptcha-settings to configure.")
            )
        return displayhtml(self.settings.public_key, language=lang)

    def verify(self):
        info = IRecaptchaInfo(self.request)
        if info.verified:
            return True

        if not self.settings.private_key:
            raise ValueError(
                _("No recaptcha private key configured. ")
                + _("Go to /@@recaptcha-settings to configure.")
            )
        response_field = self.request.get("g-recaptcha-response")
        remote_addr = self.request.get("HTTP_X_FORWARDED_FOR", "").split(",")[0]
        if not remote_addr:
            remote_addr = self.request.get("REMOTE_ADDR")
        res = submit(response_field, self.settings.private_key, remote_addr)
        if res.error_code:
            info.error = res.error_code

        info.verified = res.is_valid
        return res.is_valid
