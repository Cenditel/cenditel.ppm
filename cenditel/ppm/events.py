from zope.component import getUtility
from zope.component import getMultiAdapter
from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations
from zope.app.component.hooks import getSite

from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from Products.CMFCore.utils import getToolByName

from cenditel.ppm import CenditelPpmMF as _
from cenditel.ppm.portlets import navigation
from cenditel.ppm.portlets import select_project

from plone.portlets.constants import CONTEXT_ASSIGNMENT_KEY, CONTEXT_CATEGORY
from plone.app.portlets.storage import PortletAssignmentMapping
from smtplib import SMTPRecipientsRefused
from Products.MailHost.MailHost import MailHostError
import logging
from DateTime import DateTime


DEFAULT_RIGHT_PORTLETS = (
    ('navigation', navigation.Assignment, {}),
    ('select_project', select_project.Assignment, {}),
    )

def SavedPPM(object, evt, ):

    object.manage_setLocalRoles("PPM", ['Manager','Owner'])
    
def SavedProposal(object, evt, ):   
    date = str(DateTime())[:10]
    (Y,m,d)=str(date).split('/')
    Date=(d,m,Y)
    NText=object.getTemplatest()
    FDate='/'.join(Date)
    NText=NText.replace('$Date',FDate)
    object.setTemplatest(NText)


def SavedElement(object, evt, ):
    managers=object.getManager()
    contributors=object.Contributors()
    TotalContributors= []
    object.setContributors(managers)
    Makeportlets(object, evt)
    SendEmail(object, evt)
    AsingSuscribers(object, evt)
    
def Makeportlets(object, evt):
    annotated = IAnnotations(object)
    portlets = annotated.get(CONTEXT_ASSIGNMENT_KEY, OOBTree())

    left_portlets = portlets.get('plone.leftcolumn', PortletAssignmentMapping())
    right_portlets = portlets.get('plone.rightcolumn', PortletAssignmentMapping())

    for name, assignment, kwargs in DEFAULT_RIGHT_PORTLETS:
        if not right_portlets.has_key(name):
            right_portlets[name] = assignment(**kwargs)
            
    portlets['plone.rightcolumn'] = right_portlets
    annotated[CONTEXT_ASSIGNMENT_KEY] = portlets
    
def AsingSuscribers(object, evt):
    suscribers=list(object.getSuscribers())
    managers=object.getManager()
    list_emails = []
    
    for manager in managers:
        
        user=object.acl_users.getUserById(manager)
        email=user.getProperty('email')
        if suscribers.count(email)==0:
            list_emails.append(email)
        else:
             pass    
    suscribers.extend(list_emails)    

    object.setSuscribers(suscribers)

def SendEmail(object, evt):
    host = getToolByName(object, 'MailHost')
    message=_(u"""The project entitle %s to which you are subscribed has been modified
    you can see it in %s """) % (object.title, object.absolute_url())
    ToList=evt.object.suscribers
    From=host.smtp_userid
    Subject=_(u"Modified Content %s") % (object.title)
    if ToList == "" or ToList==[]:
        return
    else:

        try:

            host.secureSend(message, ToList, From,subject=Subject, subtype='plain', charset='UTF-8')
         
        except MailHostError:
            logger = logging.getLogger("cenditel.ppm.events.SedEmail")
            logger.warning ("We sorry, we cold not send the email because the mail host was not configure")
        except SMTPRecipientsRefused:
            logger = logging.getLogger("cenditel.ppm.events.SedEmail")
            logger.warning ("We sorry, we cold not send the email because one or more recipiendts has been refused")
            raise SMTPRecipientsRefused('Recipient address rejected by server')
