# BBB
try:
    from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
except ImportError:
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile  # noqa: F401 E501
try:
    from zope.component.hooks import getSite
except ImportError:
    from zope.app.component.hooks import getSite  # noqa: F401
try:
    from zope.browser.interfaces import IAdding
except ImportError:
    from zope.app.container.interfaces import IAdding  # noqa: F401
try:
    from zope.component.interfaces import ISite
except ImportError:
    from zope.app.component.interfaces import ISite  # noqa: F401
