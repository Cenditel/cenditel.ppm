
from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

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
    	parent = aq_base(catalog)
    	listH = []
    	for child in context.getChildNodes():
    		listH.append(child.getId())
    	
    	result = catalog.searchResults(portal_type='Project', review_state='published', getId = listH)
    	self.listt = []
    	listm = []
    	dic = []
    	for brain in result:
    		dic = brain
    		obj = dic.getObject()
    		self.listt.append(obj)
    	return self.listt
    	
Globals.InitializeClass(searching)
