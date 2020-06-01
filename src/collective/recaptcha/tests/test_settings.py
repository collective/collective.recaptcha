# encoding: utf-8
from collective.recaptcha.settings import IRecaptchaSettings
from collective.recaptcha.settings import RecaptchaSettings
from collective.recaptcha.settings import getRecaptchaSettings
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
import unittest


class TestSettings(unittest.TestCase):
    layer = COLLECTIVE_RECAPTCHA

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)

    def tearDown(self):
        try:
            settings = self.registry.forInterface(IRecaptchaSettings)
        except:
            settings = IRecaptchaSettings(self.portal)
        del settings

    def test_annotation(self):
        annotation = RecaptchaSettings(self.portal)
        annotation.public_key = u'FOO'
        annotation.private_key = u'BAR'

        settings = getRecaptchaSettings()
        self.assertEqual(u'FOO', settings.public_key)
        self.assertEqual(u'BAR', settings.private_key)

    def test_registry(self):
        self.registry.registerInterface(IRecaptchaSettings)
        settings = self.registry.forInterface(IRecaptchaSettings)
        settings.public_key = u'111'
        settings.private_key = u'222'

        settings = getRecaptchaSettings()
        self.assertEqual(u'111', settings.public_key)
        self.assertEqual(u'222', settings.private_key)
