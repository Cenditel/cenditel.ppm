#from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.utils import _createObjectByType
#from AccessControl import ClassSecurityInfo, getSecurityManager
from AccessControl import ClassSecurityInfo
from zope.interface import implements
from plone.contentrules.rule.interfaces import IExecutable
from Products.ATContentTypes.lib import constraintypes

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
                    type == 'Blog Entry'
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

                    if type == 'Folder' and title=='Events':
                        self.context.invokeFactory(type, title=title, id=title)
                        # Enable contstraining
                        self.context.setConstrainTypesMode(constraintypes.ENABLED)
                        # Types for which we perform Unauthorized check
                        self.context.setLocallyAllowedTypes(['Event'])
                        # Add new... menu  listing
                        #folder.setImmediatelyAddableTypes(["Event"])
                        # Object reindex for enabled to search
                        self.context.reindexObject()

                    elif type == 'Folder' and title=='Documents':
                        self.context.invokeFactory(type, title=title, id=title)
                        # Enable contstraining
                        self.context.setConstrainTypesMode(constraintypes.ENABLED)
                        # Types for which we perform Unauthorized check
                        self.context.setLocallyAllowedTypes(['File'])
                        # Add new... menu  listing
                        #folder.setImmediatelyAddableTypes(["File"])
                        # Object reindex for enabled to search
                        self.context.reindexObject()

                    elif type == 'Folder' and title=='Plans':
                        self.context.invokeFactory(type, title=title, id=title)
                        # Enable contstraining
                        self.context.setConstrainTypesMode(constraintypes.ENABLED)
                        # Types for which we perform Unauthorized check
                        self.context.setLocallyAllowedTypes(['File','Image','Document'])
                        # Add new... menu  listing
                        #folder.setImmediatelyAddableTypes(['File','Image','Document'])
                        # Object reindex for enabled to search
                        self.context.reindexObject()

                    if type != 'Folder':
                        self.context.invokeFactory(type, title=title, id=title)
                    '''
                    self.context.invokeFactory(type, title=title, id=title)
                    '''
                except:
                    pass
                i = i + 1
        
        return True
            
Globals.InitializeClass(CreatefolderActionExecutor) 
