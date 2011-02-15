from setuptools import setup, find_packages
import os

version = '1.1.1'

setup(name='collective.recaptcha',
      version=version,
      description="Wraps the recaptcha-client library to provide a drop-in replacement for collective.captcha.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Zope2",
        ],
      keywords='captcha recaptcha zope plone',
      author='David Glick',
      author_email='davidglick@onenw.org',
      url='http://plone.org/products/collective.recaptcha',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'recaptcha-client != 1.0.4',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
