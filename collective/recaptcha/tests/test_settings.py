# encoding: utf-8
from zope.component import getMultiAdapter
from collective.recaptcha.settings import IRecaptchaSettings
from collective.recaptcha.settings import RecaptchaSettings
from collective.recaptcha.settings import getRecaptchaSettings
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from plone.app.testing import logout
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

    def test_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='recaptcha-settings')
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse, '@@recaptcha-settings')

    def test_annotation(self):
        annotation = RecaptchaSettings(self.portal)
        annotation.public_key = u'FOO'
        annotation.private_key = u'BAR'
        annotation.multilingual = False
        annotation.default_language = u'pt'
        annotation.default_theme = u'dark'
        annotation.fallback = True

        settings = getRecaptchaSettings()
        self.assertEqual(u'FOO', settings.public_key)
        self.assertEqual(u'BAR', settings.private_key)
        self.assertEqual(False, settings.multilingual)
        self.assertEqual(u'pt', settings.default_language)
        self.assertEqual(u'dark', settings.default_theme)
        self.assertEqual(True, settings.fallback)

    def test_registry(self):
        self.registry.registerInterface(IRecaptchaSettings)
        settings = self.registry.forInterface(IRecaptchaSettings)
        settings.public_key = u'111'
        settings.private_key = u'222'
        settings.default_language = u'pt'
        settings.default_theme = u'dark'
        settings.multilingual = True
        settings.fallback = True

        settings = getRecaptchaSettings()
        self.assertEqual(u'111', settings.public_key)
        self.assertEqual(u'222', settings.private_key)
        self.assertEqual(u'pt', settings.default_language)
        self.assertEqual(u'dark', settings.default_theme)
        self.assertEqual(True, settings.multilingual)
        self.assertEqual(True, settings.fallback)
