from zope.component import getUtility
from zope.component import getMultiAdapter
from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.app.component.hooks import getSite

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from cenditel.ppm.portlets import navigation
from cenditel.ppm.portlets import select_project

from plone.portlets.constants import CONTEXT_ASSIGNMENT_KEY, CONTEXT_CATEGORY
from plone.app.portlets.storage import PortletAssignmentMapping

DEFAULT_RIGHT_PORTLETS = (
    ('navigation', navigation.Assignment, {}),
    ('select_project', select_project.Assignment, {}),
    )

def SavedElement(object, evt, ):
    managers=object.getManager()
    contributors=object.Contributors()
    TotalContributors= []
    object.setContributors(managers)
    Makeportlets(object, evt)
    
def Makeportlets(object, evt):
    annotated = IAnnotations(object)
    portlets = annotated.get(CONTEXT_ASSIGNMENT_KEY, OOBTree())

    left_portlets = portlets.get('plone.leftcolumn', PortletAssignmentMapping())
    right_portlets = portlets.get('plone.rightcolumn', PortletAssignmentMapping())
    
    #for name, assignment, kwargs in DEFAULT_LEFT_PORTLETS:
        #if not left_portlets.has_key(name):
            #left_portlets[name] = assignment(**kwargs)
    for name, assignment, kwargs in DEFAULT_RIGHT_PORTLETS:
        if not right_portlets.has_key(name):
            right_portlets[name] = assignment(**kwargs)
            
    portlets['plone.rightcolumn'] = right_portlets
    annotated[CONTEXT_ASSIGNMENT_KEY] = portlets

            
    #site = getSite()
    #column = getUtility(IPortletManager, name=u'plone.leftcolumn', context=site)
    #manager = getMultiAdapter((site, column,), IPortletAssignmentMapping)
    #import pdb; pdb.set_trace()
    
