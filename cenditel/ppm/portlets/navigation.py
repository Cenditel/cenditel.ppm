from zope.formlib import form
from zope.interface import implements
from zope.component import getMultiAdapter

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from cenditel.ppm import CenditelPpmMF as _

class INavigationPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(INavigationPortlet)

    @property
    def title(self):
        return _(u"Navigation PPM")

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('navigation.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        
    def title (self):
    	list=[]
    	holder = self.context
    	for child in holder.getChildNodes(): 
    	    list.append({child.Title():child.absolute_url()})
        return list


class AddForm(base.NullAddForm):
    form_fields = form.Fields(INavigationPortlet)
    label = _(u"Add Portlet")
    description = _(u"Navigation PPM Portlet")

    def create(self):
        return Assignment()

