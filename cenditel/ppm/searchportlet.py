from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo

import Globals

class searching:
    """
       Application which is used to find projects
       within a specified portfolio
    """
       
    security = ClassSecurityInfo()
    def __call__(self):
        pass

    security.declarePublic('searching')
    def searching(self, context):
    	catalog = getToolByName(context, 'portal_catalog')
    	listH = []
        parent=context.REQUEST['PARENTS'][1].getChildNodes()
    	for child in parent:
    		listH.append(child.getId())
    	
    	result = catalog.searchResults(portal_type='project', review_state='published', getId = listH)
    	self.listt = []
    	listm = []
    	dic = []
    	for brain in result:
    		dic = brain
    		obj = dic.getObject()
    		self.listt.append(obj)
    	return self.listt
    	
Globals.InitializeClass(searching)
