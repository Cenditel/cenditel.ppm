
from Products.CMFCore.utils import getToolByName
from StringIO import StringIO
from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES
from zope.component import getUtility
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from plone.app.controlpanel.markup import MarkupControlPanelAdapter
#from config import *
from Products.CMFCore.ActionInformation import Action
from Products.CMFCore.ActionInformation import ActionCategory
from Products.CMFCore.Expression import Expression
#from Products.CMFNotification.NotificationTool import ID as NTOOL_ID
from Acquisition import aq_inner, aq_parent, aq_base
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
from AccessControl import Unauthorized
#from Products.CMFNotification.NotificationTool import ID as NTOOL_ID
from Products.GenericSetup.context import Logger,SetupEnviron


import transaction
from shutil import copy
from os import path, getcwd

from zope.event import notify
from zope.lifecycleevent import ObjectCreatedEvent
from zope.component import createObject
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility

from cenditel.ppm import config
#from ubify.recyclebin.config import GLOBAL_RECYCLEBIN_POLICY
import string
from random import choice
import logging


def MakeDefaultUser(context, username, title,):
    
    message="""This is the default user and password for Administrator of cenditel.ppm 
    product in Portafolio Project Magnagement Content Types
    username:PPM
    password: $password
    """
    passwds=''.join([choice(string.letters + string.digits) for i in range(8)])
    print passwds
    
    site = context.getSite()
    regtool = getToolByName(site, 'portal_registration')
    passwd=None
    if passwd == None:
        #crear un password aleatorio con el scritp de ejemplo
        passwd = passwds
        properties = {
        'username' : username,
        # Full name must be always as utf-8 encoded
        'fullname' : title.encode("utf-8"),
        'email' : 'ppmadmin@admin.com',
    	}
    logger = logging.getLogger("SetupHandlers.cenditel.ppm")
    try:
        
        member = regtool.addMember(username, passwd, properties=properties)
        storages = file("userPPM.txt", "w")
        message=message.replace('$password',passwds)
        storages.write(message)
        storages.close()
        logger.info("User PPM create, go to userPPM.txt")
    except:
        logger.warning("We have a failure trying to create a user for cenditel.ppm product")
    return None
    
def configureCMFNotification(portal,logger):
    """
    TODO fix problem with zcatalog after launch this method
    """
    ntool = getToolByName(portal, NTOOL_ID)
    changeProperty = lambda key, value: \
            ntool.manage_changeProperties(**{key: value})
    
    if not ntool.isExtraSubscriptionsEnabled():
        changeProperty('extra_subscriptions_enabled',True)
    #enable notification on Item creation
    
    changeProperty('item_creation_notification_enabled', True)
    changeProperty('on_item_creation_mail_template',['* :: string:creation_mail_notification'])
    logger.info("On Item Creation Notification has been enabled.")
    
    #enable notification on Item modification
    changeProperty('item_modification_notification_enabled', True)
    changeProperty('on_item_modification_mail_template',['* :: string:modification_mail_notification'])
    logger.info("On Item Modification Notification has been enabled.")
    
    #enable notification on Work Flow Transition
    changeProperty('wf_transition_notification_enabled', True)
    changeProperty('on_wf_transition_mail_template',['* :: string:workflow_mail_notification'])
    logger.info("On Workflow transition Notification has been enabled.")
    
    #enable notification on Discussion Item Creation
    changeProperty('discussion_item_creation_notification_enabled',True)
    changeProperty('on_discussion_item_creation_mail_template',['* :: string:discussion_mail_notification'])
    logger.info("On Discussion Item Creation Notification has been enabled.")   
    

def importVarious(context):
    """Miscellanous steps import handle
    """
    #VAMOS A PONERLA EN EL CONFIG
    USERNAME='PPM'
    username=USERNAME
    title='cenditel.ppm'
    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a 
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('cenditel.ppm.txt') is None:
        return

    portal = context.getSite()
    obj = SetupEnviron()   
    logger = obj.getLogger("cenditel.ppm")
    MakeDefaultUser(context, username, title)
    #TODO configureCMFNotification(portal,logger)    

