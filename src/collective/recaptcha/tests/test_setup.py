# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING
from Products.CMFPlone.browser.admin import AddPloneSite
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.recaptcha is properly installed."""

    layer = COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.installer = get_installer(self.portal, self.request)

    def test_hide_extensions_profiles(self):
        """The only installable profile must be collective.recaptcha:default"""
        app = self.layer["app"]
        add_plone_site = AddPloneSite(app, self.request)
        profiles = add_plone_site.profiles()
        extensions_profiles = profiles["extensions"]
        profiles_ids = [profile["id"] for profile in extensions_profiles]
        recaptcha_profiles = [
            profile_id
            for profile_id in profiles_ids
            if profile_id.startswith("collective.recaptcha")
        ]
        self.assertEqual(["collective.recaptcha:default"], recaptcha_profiles)
