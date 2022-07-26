# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.recaptcha.settings import IRecaptchaSettings
from collective.recaptcha.testing import COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING
from plone.api.portal import get_registry_record
from plone.api.portal import get_tool
from plone.api.portal import set_registry_record
from plone.api.user import get_roles
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.recaptcha is properly installed."""

    layer = COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_tool("portal_quickinstaller")

    def reapply_profile(self):
        set_registry_record("public_key", u"111", IRecaptchaSettings)
        set_registry_record("private_key", u"222", IRecaptchaSettings)
        portal_setup = get_tool("portal_setup")
        portal_setup.runAllImportStepsFromProfile(
            "profile-collective.recaptcha:default"
        )

    def test_product_installed(self):
        """Test if collective.recaptcha is installed."""
        self.assertTrue(self.installer.isProductInstalled("collective.recaptcha"))

    def test_keep_public_key_in_reapply_profile(self):
        self.reapply_profile()
        self.assertEqual(
            u"111",
            get_registry_record("public_key", IRecaptchaSettings),
        )

    def test_keep_private_key_in_reapply_profile(self):
        self.reapply_profile()
        self.assertEqual(
            u"222",
            get_registry_record("private_key", IRecaptchaSettings),
        )


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_tool("portal_quickinstaller")
        roles_before = get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(products=["collective.recaptcha"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.recaptcha is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("collective.recaptcha"))
