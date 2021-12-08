# encoding: utf-8
from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import PloneWithPackageLayer

import collective.recaptcha


COLLECTIVE_RECAPTCHA = PloneWithPackageLayer(
    zcml_filename="configure.zcml",
    zcml_package=collective.recaptcha,
    additional_z2_products=(),
    bases=(PLONE_INTEGRATION_TESTING,),
    name="COLLECTIVE_RECAPTCHA",
)
