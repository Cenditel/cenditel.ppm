from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from zope.app.component.hooks import getSite

def SavedElement(object, evt, ):
    managers=object.getManager()
    contributors=object.Contributors()
    TotalContributors= []
    object.setContributors(managers)
    #Makeportlets(object, evt)
    
#def Makeportlets(object, evt):
    #site = getSite()
    #column = getUtility(IPortletManager, name=u'plone.leftcolumn', context=site)
    #manager = getMultiAdapter((site, column,), IPortletAssignmentMapping)
    #import pdb; pdb.set_trace()
    
