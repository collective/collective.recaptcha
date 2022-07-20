# encoding: utf-8
"""Tests of view."""
from collective.recaptcha import PLONE4
from collective.recaptcha.settings import IRecaptchaSettings
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING
from plone.api.content import get_view
from plone.api.portal import set_registry_record

import unittest


class TestView(unittest.TestCase):
    layer = COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        set_registry_record("public_key", u"111", IRecaptchaSettings)
        set_registry_record("private_key", u"222", IRecaptchaSettings)
        self.view = get_view("captcha", self.portal, self.request)

    def test_image_tag(self):
        image_tag = self.view.image_tag()
        self.assertIn(
            "https://www.google.com/recaptcha/api.js?hl=en&fallback=False&", image_tag
        )
        self.assertIn('data-sitekey="111"', image_tag)

    def test_image_tag_extra_script_not_in_normal_request(self):
        image_tag = self.view.image_tag()
        self.assertNotIn("<script>", image_tag)

    @unittest.skipUnless(PLONE4, "Relevant only for Plone 4")
    def test_image_tag_extra_script__in_ajax_request_plone4(self):
        self.request.set("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
        image_tag = self.view.image_tag()
        self.assertIn("<script>", image_tag)

    @unittest.skipIf(PLONE4, "Relevant only for Plone >= 5")
    def test_image_tag_extra_script__not_in_ajax_request_plone5(self):
        self.request.set("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
        image_tag = self.view.image_tag()
        self.assertNotIn("<script>", image_tag)

    def test_verify(self):
        self.assertFalse(self.view.verify())

    def test_verify_remote_addr(self):
        self.request["REMOTE_ADDR"] = "localhost"
        self.assertFalse(self.view.verify())

    def test_verify_http_x_forwarded_for(self):
        self.request["HTTP_X_FORWARDED_FOR"] = "localhost1, localhost2"
        self.assertFalse(self.view.verify())
