"""Definition of the folderproj content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from cenditel.ppm.validator import EvilValidator
#from validator import EvilValidator

from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm.interfaces import Ifolderproj
from cenditel.ppm.config import PROJECTNAME
from Products.DataGridField import DataGridField, DataGridWidget


folderprojSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    DataGridField('group',
        schemata='Grups',
        required= 1,
        validators = ('evilness',),
		default=({'title' : '', 'Description' : ''},),
        widget = DataGridWidget(
        description=_(u"Enter a list of groups (departments / communities / sections) within this portfolio."),),
        columns=(_(u'Title'),_(u'Description'))
        
        ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

folderprojSchema['title'].storage = atapi.AnnotationStorage()
folderprojSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    folderprojSchema,
    folderish=True,
    moveDiscussion=False
)


class folderproj(folder.ATFolder):
    """folder projects"""
    implements(Ifolderproj)

    meta_type = "folderproj"
    schema = folderprojSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(folderproj, PROJECTNAME)
