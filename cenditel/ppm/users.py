from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFCore.utils import getToolByName
#from Products.PluggableAuthService.interfaces.authserve.IPluggableAuthService import searchUsers
#from Products.PluggableAuthService.interfaces import IPluggableAuthService as IPAS

from cenditel.ppm.interfaces import IProject

def userVocabularyFactory(context):
    """Vocabulary factory to find all registered users
    
    @param context: application context
    
    @return: values
    """
    users = context.acl_users.getUserIds()
    #users = IPAS.searchUsers()
    i = 0
    items = []
    for user in users:
        if len(users)==1:
            items.append((user,user))
            break
        else:
            items.append((user,user))
    tuple_items = tuple(items)
    values = SimpleVocabulary.fromItems(tuple_items)    
    return values

directlyProvides(userVocabularyFactory, IVocabularyFactory)
