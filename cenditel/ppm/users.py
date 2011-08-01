from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

from Products.CMFCore.utils import getToolByName


from cenditel.ppm.interfaces import IProject

def userVocabularyFactory(context):
    """Vocabulary factory to find all registered users
    
    @param context: application context
    
    @return: values
    """
    users=context.acl_users.getUsers()
    i = 0
    items = []
    for user in users:
        userid=user.getUserId()
        if len(users)==1:
            items.append((userid,userid))
            break
        else:
            items.append((userid,userid))
    tuple_items = tuple(items)
    values = SimpleVocabulary.fromItems(tuple_items)    
    return values

directlyProvides(userVocabularyFactory, IVocabularyFactory)
