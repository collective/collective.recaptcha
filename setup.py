from setuptools import setup, find_packages
import os

version = '2.0.0'

setup(name='collective.recaptcha',
      version=version,
      description="Wraps the recaptcha-client library to provide a drop-in replacement for collective.captcha.",
      long_description=(open("README.rst").read() + "\n" +
                        open(os.path.join("docs", "HISTORY.txt")).read()),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: Zope2",
          "Framework :: Plone",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='captcha recaptcha zope plone',
      author='David Glick',
      author_email='david@glicksoftware.com',
      url='http://github.com/collective/collective.recaptcha',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'norecaptcha',
          'Plone',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
          ]},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
