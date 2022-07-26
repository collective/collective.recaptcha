# -*- coding: utf-8 -*-
"""Installer for the collective.recaptcha package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="collective.recaptcha",
    version="2.1.2",
    description="Wraps the recaptcha-client library to provide a drop-in "
    "replacement for collective.captcha.",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="captcha recaptcha zope Python Plone",
    author="David Glick",
    author_email="david@glicksoftware.com",
    url="https://github.com/collective/collective.recaptcha",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/collective.recaptcha",
        "Source": "https://github.com/collective/collective.recaptcha",
        "Tracker": "https://github.com/collective/collective.recaptcha/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        "norecaptcha",
        "Plone >=4.3",
        "Products.CMFCore",
        "Products.CMFPlone",
        "setuptools",
        "zope.component",
        "zope.i18nmessageid",
    ],
    extras_require={
        "test": [
            "plone.api",
            "plone.app.testing",
            "plone.testing>=5.0.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.recaptcha.locales.update:update_locale
    """,
)
