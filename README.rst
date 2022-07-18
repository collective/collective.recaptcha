collective.recaptcha
====================

This package provides an integration of the reCAPTCHA service into Zope.
ReCAPTCHA is a third-party CAPTCHA service provided by Google.

The API is provided via a "@@captcha" browser view.

Plone users interested in adding ReCAPTCHA in z3c.form forms
will probably find interesting the package
`plone.formwidget.recaptcha <https://github.com/plone/plone.formwidget.recaptcha>`_.

Upgrade
-------

To upgrade to collective.recaptcha 2.* (reCaptcha API V2), you need double check your keys
because global keys are not supported in the V2 API, so you need to create a new key
if you wish to use the V2 API.

Installation and Configuration
------------------------------

Simply make sure that the ZCML for this package is loaded.  (You cannot configure
this package at the same time as collective.captcha, because the '@@captcha'
browser view registration will conflict.)

Before the service will work, you must obtain a public and private key from
https://developers.google.com/recaptcha/, and configure them at
http://path/to/site/@@recaptcha-settings

You can use plone.app.registry in your profile to provide your configuration::

  <registry>
    <records interface="collective.recaptcha.settings.IRecaptchaSettings">
     <value key="public_key"></value>
     <value key="private_key"></value>
    </records>
  </registry>


Usage
-----

You can insert a Recaptcha using the following TAL::

  <tal:block tal:replace="structure python:context.restrictedTraverse('@@captcha').image_tag()"/>

You can verify Recaptcha input by testing the return value of::

  context.restrictedTraverse('@@captcha').verify()


Tests
-----

This add-on is tested using GitHub Actions. The current status of the add-on is :

.. image:: https://img.shields.io/github/workflow/status/collective/collective.recaptcha/Plone%20package/master?label=GitHub%20Actions
    :target: https://github.com/collective/collective.recaptcha/actions/workflows/plone-package.yml
