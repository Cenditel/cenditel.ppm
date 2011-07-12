from zope.interface import implements, Interface
	
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.utils import _createObjectByType
	
from cenditel.ppm import CenditelPpmMF as _
from cenditel.ppm import createSubFolder
from cenditel.ppm.config import SCHEDULE_STATUS_PROJECT, BUDGET_STATUS_PROJECT
	
class Iprojectview(Interface):
    """
    project view interface
    """
    
    def test():
        """ test method """
    
class projectview(BrowserView):
    """
    project browser view
    """

    implements(Iprojectview)
	
    def __init__(self, context, request):
        self.context = context
	self.request = request
	

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')
	
    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()


    def subfol(self):
        """ 
        Run the script for the creation of sub folders
        """
        m = createSubFolder.CreatefolderActionExecutor(self.context)
        m.sub()
        return 
        
    def GetBeginDate(self):
        (Y,m,d)=str(self.context.getBegin_date()).split('/')
        Date=(d,m,Y)
        beginDate='/'.join(Date)
        return beginDate
        
    def GetEndDate(self):
        (Y,m,d)=str(self.context.getEnd_date()).split('/')
        Date=(d,m,Y)
        endDate='/'.join(Date)
        return endDate
        
 
    def roles(self):
        """
        assigned the role of Owner the selected user
        """
        members = list(self.context.getManager())
        roles = self.context.get_local_roles()
        list_all_users=members
        userwithroles=[]
        for i in range(len(roles)):
            userwithroles.append(roles[i][0])
        #import pdb; pdb.set_trace()
        list_all_users.extend(userwithroles)
        for member in list_all_users:
            
            if member in userwithroles:
                pass
            else:
                self.context.manage_setLocalRoles(member, ['Owner'])
            if not member in (self.context.getManager()):
                self.context.manage_delLocalRoles([member,])
        return None
		
    def validator(self):
        holder = self.context
        value1=holder.getCompleted()
        value2=holder.est_budget
        value3=holder.act_budget
        if value1 == "":
            holder.setCompleted("0")
        if value2 == "":
            holder.setEst_budget("0")
        if value3 == "":
            holder.setAct_budget("0")
        
        return None
		
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
		
        
    def blog(self):
        
        try:
            holder = self.context
            catalog = getToolByName(holder, 'portal_catalog')
            List = []

            blogs = getattr(holder,"Weblog")
            URL = blogs._getURL()
            for child in blogs.getChildNodes(): 
                List.append(child.getId())
                
            result = catalog.searchResults(portal_type='WeblogEntry', review_state='published', getId = List)
            dic = []
            ListA = []
            for brain in result:
                dic = brain
                obj = dic.getObject()
                ListA.append(obj)
            return ListA
        except:
            return ""			
