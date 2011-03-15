#from zope.component import getMultiAdapter
#from zope.component import getUtility
#from plone.i18n.normalizer.interfaces import IIDNormalizer
#from Products.Five import BrowserView
#from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from AccessControl import ClassSecurityInfo, getSecurityManager
#from Acquisition import aq_base, aq_inner, aq_parent
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
