from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IPPM(Interface):
    """A Folder dedicate to proposals and projects"""

class IPPMSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 skin layer 
       for this product."""
