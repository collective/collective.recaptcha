# encoding: utf-8
from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import PloneWithPackageLayer

import collective.recaptcha


COLLECTIVE_RECAPTCHA_INTEGRATION_TESTING = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.recaptcha,
    gs_profile_id="collective.recaptcha:default",
    additional_z2_products=(),
    bases=(PLONE_INTEGRATION_TESTING,),
    name="COLLECTIVE_RECAPTCHA",
)
