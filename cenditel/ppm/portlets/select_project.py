from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from zope.interface import implements
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.formlib import form

from cenditel.ppm import ppmMessageFactory as _

class INavigationPortlet(IPortletDataProvider):
    pass

class Assignment(base.Assignment):
    implements(INavigationPortlet)

    @property
    def title(self):
        return _(u"Projects Dashboard")

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('select_project.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        
    def title (self):
    	list=[]
    	holder=self.context
    	for child in holder.getChildNodes(): 
    	    list.append({child.Title():child.absolute_url()})
        return list


class AddForm(base.NullAddForm):
    form_fields = form.Fields(INavigationPortlet)
    label = _(u"Add Portlet")
    description = _(u"Projects Dashboard Portlet")

    def create(self):
        return Assignment()

