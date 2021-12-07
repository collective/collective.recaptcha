# coding=utf-8

# BBB
try:
    from zope.component.hooks import getSite
except ImportError:
    from zope.app.component.hooks import getSite  # noqa: F401
try:
    from zope.component.interfaces import ISite
except ImportError:
    from zope.app.component.interfaces import ISite  # noqa: F401
