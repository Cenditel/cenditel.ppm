from zope.component import getMultiAdapter
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from AccessControl import ClassSecurityInfo, getSecurityManager
from Acquisition import aq_base, aq_inner, aq_parent

import Globals

class searching:
    """application which is used to find projects
        within a specified portfolio"""
       
    security = ClassSecurityInfo()
    def __call__(self):
        pass
    security.declarePublic('searching')
    def searching(self, context):
    	catalog = getToolByName(context, 'portal_catalog')
    	parent = aq_base(catalog)
    	listaH=[]
    	for child in context.getChildNodes():
    		listaH.append(child.getId())
    	
    	result=catalog.searchResults(portal_type='project', review_state='published', getId = listaH)
    	self.listat=[]
    	listam=[]
    	dic=[]
    	for brain in result:
    		dic=brain
    		obj=dic.getObject()
    		self.listat.append(obj)
    	return self.listat
    	
Globals.InitializeClass(searching)
