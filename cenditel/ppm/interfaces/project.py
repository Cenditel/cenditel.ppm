from zope import schema
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer
from cenditel.ppm import ppmMessageFactory as _

class Iproject(Interface):
    """projects"""

    # -*- schema definition goes here -*-

class IprojectSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer 
       for this product."""
