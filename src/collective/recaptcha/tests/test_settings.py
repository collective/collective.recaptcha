# encoding: utf-8
from collective.recaptcha.settings import getRecaptchaSettings
from collective.recaptcha.settings import IRecaptchaSettings
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class TestSettings(unittest.TestCase):
    layer = COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.registry = getUtility(IRegistry)

    def test_registry(self):
        self.registry.registerInterface(IRecaptchaSettings)
        settings = self.registry.forInterface(IRecaptchaSettings)
        settings.public_key = u"111"
        settings.private_key = u"222"

        settings = getRecaptchaSettings()
        self.assertEqual(u"111", settings.public_key)
        self.assertEqual(u"222", settings.private_key)
