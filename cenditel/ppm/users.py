#from Products.CMFCore.utils import getToolByName
#from cenditel.ppm.interfaces import Iproject
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

def userVocabularyFactory(context):
    """Vocabulary factory to find all registered users
    
    @param context: application context
    
    @return: values
    """
    users = context.acl_users.getUserIds()
    i = 0
    #lista = []
    items = []
    for user in users:
        if len(users)==1:
            break
        else:
            i+=1

            items.append((user,user))
    tuple_items = tuple(items)
    values = SimpleVocabulary.fromItems(tuple_items)    
    return values

directlyProvides(userVocabularyFactory, IVocabularyFactory)
