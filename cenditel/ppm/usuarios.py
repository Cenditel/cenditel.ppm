from Products.Archetypes.utils import DisplayList
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from cenditel.ppm.interfaces import Iproject
from Products.CMFCore.utils import getToolByName



def usuarioVocabularyFactory(context):
    """Vocabulary factory to find all registered users
    """
    usuarios = context.acl_users.getUserIds()
    i=0
    lista=[]
    items=[]
    for usuario in usuarios:
        if len(usuarios)==1:
            break
        else:
            i+=1

            items.append((usuario,usuario))
    tuplaitems=tuple(items)
    values=SimpleVocabulary.fromItems(tuplaitems)    
    return values


directlyProvides(usuarioVocabularyFactory, IVocabularyFactory)
