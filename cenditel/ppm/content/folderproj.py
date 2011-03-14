"""Definition of the folderproj content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.DataGridField import DataGridField, DataGridWidget

from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm.config import PROJECTNAME
from cenditel.ppm.interfaces import Ifolderproj
from cenditel.ppm.validator import GroupsValidator

folderprojSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    DataGridField(
        name='group',
        widget = DataGridWidget(
            label=_(u"Groups"),
            description=_(u"Enter a list of groups (departments / communities / sections) within this portfolio."),
        ),
        schemata='Groups',
        required=True,
        validators = ('isGroups',),
        default=(
            { 
             'title' : '', 
             'Description' : ''
            },
        ),
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
    """A Folder dedicate to proposals and projects"""
    implements(Ifolderproj)

    meta_type = "folderproj"
    schema = folderprojSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(folderproj, PROJECTNAME)
