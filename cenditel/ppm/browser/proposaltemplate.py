from DateTime import DateTime

from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from Acquisition import aq_base, aq_inner, aq_parent

from cenditel.ppm.interfaces import Ifolderproj
from Products.Archetypes.utils import DisplayList
from DateTime import DateTime


class proposaltemplateview(BrowserView):

    template = ViewPageTemplateFile('templates/porposalselecttemplate.pt')
    
    def __init__(self, context, request):
         self.context=context
         self.request=request
         return
    
    def __call__(self):
        self.request.set('disable_border', True)
        return self.template()
        
    def groups(context):
        """Vocabulary factory for currently published films
        """
        listaG=[]
        Dic=context.context.getGroup()
        i=0
        
        for x in Dic:
            qq=Dic[i].values()[1]
            listaG.append((qq,qq))
            i+=1
        tuplegrup=tuple(listaG)
        LISTG = DisplayList(tuplegrup)
        
        return LISTG
        
        
    def searchtemplates(context):
        """Vocabulary factory for currently published films
        """
        catalog = getToolByName(context, 'portal_catalog')
        templates=getattr(context.context, "Templates")
        listaH=[]
        listaT=[]
        for hijo in templates.getChildNodes():
            listaH.append(hijo.getId())
            Titlep=hijo.Title()
            listaT.append((Titlep, Titlep))
        
        tupla=tuple(listaT)
        LIST = DisplayList(tupla)
        
        return LIST
        
    def newproposalss(self):
        holder=self.context
        year = str(DateTime())[:4]
        date = str(DateTime())[:10]
        year = '%s' % (year)
        date = '%s' % (date)
        if self.request.form.has_key('form.button.cancel'):
            
            C_url=holder.absolute_url()
            return self.request.RESPONSE.redirect(C_url) 
        else:
            pass

        
        try:
            proposal=self.request.form["proposal_type"]
            Sgroup=self.request.form["Group"]
            Tit=self.request.form["subj"]
            proposal=proposal.lower()
            
            title = '%s %s' % (Tit, year)
            folder=getattr(holder,"Templates") 
            hhh=getattr(folder, proposal)
            
            body=hhh.getText()
            body=body.replace("$Date", str(DateTime())[:10])  
            body=body.replace("$Group", Sgroup)
            body=body.replace("$Subject", Tit)
            
            
            holder.invokeFactory('proposals', title=title, id=title)
            propo = getattr(holder, title)
            propo.setTemplatest(body)
            url = propo.absolute_url() + ("/edit")
            return self.request.RESPONSE.redirect(url)
        except:
            pass
            return
            
