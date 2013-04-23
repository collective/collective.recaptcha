
from zope.component import queryMultiAdapter

from zope.formlib.interfaces import MissingInputError
from zope.formlib.interfaces import WidgetInputError

from zope.formlib.textwidgets import TextWidget

from collective.recaptcha.bbb import getSite


class ReCaptchaWidget(TextWidget):

    def __call__(self):
        captcha = queryMultiAdapter((self.context, self.request),
                                    name="captcha")
        if captcha:
            widget = captcha.image_tag()
        else:
            widget = ""
        return widget

    def hasInput(self):
        return 'recaptcha_response_field' in self.request.form

    def getInputValue(self):
        self._error = None

        # form input is required, otherwise raise an error
        if not self.hasInput():
            raise MissingInputError(self.name, self.label, None)

        site = getSite()
        valid_captcha = site.restrictedTraverse('@@captcha').verify()

        if not valid_captcha:
            self._error = WidgetInputError(self.context.__name__,
                                           self.label,
                                           "")
            raise self._error
        return
