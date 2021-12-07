collective.recaptcha
====================

This package provides an integration of the reCAPTCHA service into Zope.
ReCAPTCHA is a third-party CAPTCHA service provided by Google.

The API is based on collective.captcha and is provided via a "@@captcha"
browser view, so these two packages can be swapped for each other relatively
simply.  Use collective.captcha if you need to not be dependent on an external
service; use collective.recaptcha for a slightly better user experience.

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

  <tal:block tal:replace="structure context/@@captcha/image_tag"/>

You can verify Recaptcha input by testing the return value of::

  context.restrictedTraverse('@@captcha').verify()


Differences between this package's API and collective.captcha
-------------------------------------------------------------

Because the simplest form of Recaptcha is rendered entirely via a remote call
to the service, we couldn't implement the ICaptchaView interface from
collective.captcha exactly as it was defined there.
Differences include::

  * The image_tag method returns the HTML for the entire CAPTCHA widget,
    including text entry and audio link, not just the tag for the CAPTCHA
    image.

  * The audio_url method returns None

  * The verify method does not require the input parameter, as a standard
    form input name is used and the value can be found in the request.

  * There is an additional method, external, which simply returns True.
    This is a bit of a hack so that a template requiring captcha can
    adjust to the different semantics of the @@captcha view in this
    package as compared to collective.captcha.

Tests
-----

This add-on is tested using GitHub Actions. The current status of the add-on is :

.. image:: https://img.shields.io/github/workflow/status/collective/collective.recaptcha/Plone%20package/master?label=GitHub%20Actions
    :target: https://github.com/collective/collective.recaptcha/actions/workflows/plone-package.yml
