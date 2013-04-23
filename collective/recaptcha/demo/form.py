
from five.formlib.formbase import PageForm

from zope.formlib import form
from zope.interface import Interface
from zope import schema

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.recaptcha.formlib_widget import ReCaptchaWidget


class IReCaptcha(Interface):
    name = schema.TextLine(title=u"Name")
    captcha = schema.TextLine(title=u"ReCaptcha")


class ReCaptchaForm(PageForm):
    label = u""
    description = u""
    form_fields = form.Fields(IReCaptcha)
    form_fields["captcha"].custom_widget = ReCaptchaWidget
    template = ViewPageTemplateFile('form.pt')

    @form.action(u'Submit', name=u'submit')
    def action_submit(self, action, data):
        return self.request.response.redirect(
            self.context.absolute_url()+"/recaptcha-demo")
