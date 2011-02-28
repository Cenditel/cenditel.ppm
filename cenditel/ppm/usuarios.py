from Products.Archetypes.utils import DisplayList
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from cenditel.ppm.interfaces import Iproject
from Products.CMFCore.utils import getToolByName



def userVocabularyFactory(context):
    """Vocabulary factory to find all registered users
    """
    users = context.acl_users.getUserIds()
    i=0
    lista=[]
    items=[]
    for user in users:
        if len(users)==1:
            break
        else:
            i+=1

            items.append((user,user))
    tuplaitems=tuple(items)
    values=SimpleVocabulary.fromItems(tuplaitems)    
    return values


directlyProvides(userVocabularyFactory, IVocabularyFactory)
