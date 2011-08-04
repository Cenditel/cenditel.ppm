from zope.interface import implements, Interface
	
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.utils import _createObjectByType
from Products.ATContentTypes.lib import constraintypes
	
from cenditel.ppm import CenditelPpmMF as _
from cenditel.ppm import search
from cenditel.ppm.config import SCHEDULE_STATUS_PROJECT, BUDGET_STATUS_PROJECT
from cenditel.ppm.Image import DefaultImage
	
class IPPMView(Interface):
    """
    proj view interface
    """
    
    def test():
        """ test method """
    
class PPMView(BrowserView, object):
    """
    proj browser view
    """

    implements(IPPMView)
	
    def __init__(self, context, request):
        self.context = context
	self.request = request
	
    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
	
    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()
    

    def searching(self):
        z=search.searching()
        self.result=z.searching(self.context)
        return self.result
        
    def GetManagers(self):
        Manag=[]
        NewListManag=[]
        for NM in self.result:
            managerobject= NM.getManager()
            Manag.extend(managerobject)
            
        for x in Manag:
            if not x in NewListManag:
                NewListManag.append(x)
            else:
                pass
        return NewListManag
       
       

    def GetStatus(self):
        RealStatus={}
        for TupleStatus in SCHEDULE_STATUS_PROJECT.items():
            RealStatus[TupleStatus[0]]=self.context.translate(SCHEDULE_STATUS_PROJECT.getMsgId(TupleStatus[0]))
        #import pdb; pdb.set_trace()
        return RealStatus

    def GetBud(self):
        RealBud={}
        for TupleBud in BUDGET_STATUS_PROJECT.items():
            RealBud[TupleBud[0]]=self.context.translate(BUDGET_STATUS_PROJECT.getMsgId(TupleBud[0]))
        #import pdb; pdb.set_trace()
        return RealBud

    def GetTags(self):
        """
        the tag list that are within the portfolio of projects
        """
        tagsList=[]
    	for element in self.result:
    	    tagsList.extend(element.getTags())
        return tagsList

    def createfol(self):
        """
        Create the containing folder of the proposals
        and a template 
        """
        holder = self.context
        txt = """Subject: 



Email: 

Telephone:

Fax:

Date Request Submitted (YYYY/MM/DD): $Date

Note: The newProposal script will substiute $Subject, $Group, and $Date
with appropriate values from the form regardless of where they are in the template.

To create a new proposal type, you can copy and paste this or any other template
and its associated Dashboard wiki page, rename it appropriately, and modify its
contents with the information you want collected.

"""
        try:
            '''
            self.context.invokeFactory("Folder", title="Proposal Templates", id="Templates")
            # Enable contstraining
            self.context.setConstrainTypesMode(constraintypes.ENABLED)
            # Types for which we perform Unauthorized check
            self.context.setLocallyAllowedTypes(['FCKTemplate'])
            # Add new... menu  listing
            folder.setImmediatelyAddableTypes(['FCKTemplate'])
            # Object reindex for enabled to search
            self.context.reindexObject()
            
            foldert = getattr(holder, "Templates")
            foldert.invokeFactory("FCKTemplate", title="Example", id="example")
            
            example = getattr(foldert, "example")
            example.setText(txt)
            '''
            self.context.invokeFactory("Folder", title="Proposal Templates", id="Templates")
            
            foldert=getattr(holder, "Templates")
            foldert.setConstrainTypesMode(constraintypes.ENABLED)
            foldert.setLocallyAllowedTypes(['FCKTemplate'])
            foldert.invokeFactory("FCKTemplate", title="Example", id="example", anIcon=DefaultImage())
            example=getattr(foldert, "example")
            example.setText(txt)
        except:
            pass
        return 


    def MyDate(self, OriginalDate):
        (Y,m,d)=str(OriginalDate).split('/')
        Date=(d,m,Y)
        NewDate='/'.join(Date)
        return NewDate
