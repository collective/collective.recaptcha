Changelog
=========

3.0.0 (unreleased)
------------------

- Removes compatibility with ``collective.captcha``.
  [wesleybl]

- No longer reads settings in annotation in portal root.
  [wesleybl]

- Remove attempt to use ``five.formlib`` in controlpanel form. Now only Plone 5.2 is supported.
  [wesleybl]

- Add support to Python 3.6, 3.7 and 3.8.
  [wesleybl]

- Drop support to Plone 4.3 and Plone 5.0.
  [wesleybl]

- Add support to Plone 5.2.
  [wesleybl]

- Drop support to Plone 4.2
  [idgserpro]


2.1.2 (2022-07-26)
------------------

- Keep record values when reapplying profile (fixes `#36 <https://github.com/collective/collective.recaptcha/issues/36>`_).
  [wesleybl]


2.1.1 (2022-07-21)
------------------

- Fix recaptcha loading in Plone 4 modal.
  [wesleybl]

- Fixed startup on Python 3 (Plone 5.2).
  The tests are not run yet on 5.2, so compatibility is not confirmed.
  [maurits]

- Add translations
  [rodfersou]


2.1.0 (2017-12-04)
------------------

- Updated bootstrap
- Updated the documentation
- Support Plone 5 without the need to pull in zope.formlib
  [ale-rt]

- Add install and uninstall profile and a controlpanel configlet
  [frapell]


2.0.0 (2016-03-06)
------------------

- Google reCAPTCHA API v.2
  [mamico]


1.1.5 (2014-05-07)
------------------

- Fix the retrieval of config from the registry
  [mpeeters]

- Minor correction in interface name, in the README
  [frapell]


1.1.4 (2013-04-09)
------------------

- Add Plone 4.3 compat
  [aclark4life]


1.1.3 (2011-08-19)
------------------

- Add `z3c.autoinclude` entry point for automatic ZCML loading in Plone 3.3+.
  [WouterVH]


1.1.2 (2011-05-17)
------------------

- Require the latest version of recaptcha-client, which has the correct HTTPS
  URL for the recaptcha service.
  [davisagli]

- Add support for Zope2.13: try to use five.formlib first.
  [toutpt]


1.1.1 (2011-02-15)
------------------

- Register the @@captcha view using browser:page instead of browser:view,
  because I still fail to understand the latter and was breaking access from
  restricted python in Zope 2.12.
  [davisagli]


1.1 (2010-11-18)
----------------

- Use the recaptcha settings from plone.formwidget.recaptcha if it is
  installed, since it overrides our recaptcha-settings view.
  [davisagli]


1.0.1 (2009-08-05)
------------------

- Disallowed dependency on broken release of recaptcha-client (1.0.4).
  [davisagli]


1.0 (2009-05-04)
----------------

- Fixed method signature for verify method so that the vestigial input parameter
  from collective.captcha's ICaptchaView is no longer required.
  [davisagli]

- Added documentation.
  [davisagli]


1.0b2 (2009-01-14)
------------------

- Correctly handle comma-delimited values in the HTTP_X_FORWARDED_FOR
  header.
  [davisagli]

- Added support for verifying the captcha multiple times within the same request.
  [davisagli]

- Added security declarations on the view methods so they can be called from
  restricted Python.
  [davisagli]


1.0b1 (2009-01-14)
------------------

- Initial release

