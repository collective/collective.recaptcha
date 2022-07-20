# coding=utf-8
from Products.CMFPlone.utils import getFSVersionTuple
from zope.i18nmessageid import MessageFactory


RecaptchaMessageFactory = MessageFactory("collective.recaptcha")

PLONE4 = getFSVersionTuple()[0] == 4
