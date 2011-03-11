from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
from AccessControl import ClassSecurityInfo, getSecurityManager
from zope.interface import implements
from plone.contentrules.rule.interfaces import IExecutable

import Globals

class CreatefolderActionExecutor(object):
    """ This application is used to create all sub-folders 
        inside of the projects"""
    security = ClassSecurityInfo()

    implements(IExecutable)
    def __init__(self, context):
        self.context = context
        return

    security.declarePublic('sub')
    def sub(self): 
        dic = self.context.getProject_folders()
        i = 0
        try:
            import ubifiy.policy
            for x in dic:
                type = dic[i].values()[0] 
                title = dic[i].values()[1] 
                if type == 'Ploneboard' and title=='Discussion':
                    type == 'Discussion'
                if type == 'Weblog' and title== 'Weblog':
                    type=='Blog Entry'
                try:
                    self.context.invokeFactory(type, title=title, id=title)
                except:
                    pass            
                i = i + 1
        except ImportError:
            for x in dic:
                type = dic[i].values()[0]
                title = dic[i].values()[1]
                try:
                    self.context.invokeFactory(type, title=title, id=title)
                except:
                    pass
                i = i + 1
        
        return True
            
Globals.InitializeClass(CreatefolderActionExecutor) 
