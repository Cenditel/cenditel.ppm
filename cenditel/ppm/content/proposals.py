"""Definition of the proposals content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cenditel.ppm.interfaces import Iproposals
from cenditel.ppm.config import PROJECTNAME
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from Products.Archetypes.utils import Message


proposalsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((


    atapi.TextField(
    name='templatest',
    default_content_type = 'text/restructured',
    storage=atapi.AnnotationStorage(),
    default_output_type = 'text/x-html-safe',
    allowable_content_types=('text/plain', 'text/restructured', 'text/html',),
    default='',
    #vocabulary_factory="cenditel.ppm.prop",
    widget=atapi.RichWidget(
        
        label="Summary",
        description="template of the proposal",
        rows="10",
    ),
    searchable=1,
    required=0
),



))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

proposalsSchema['title'].storage = atapi.AnnotationStorage()
proposalsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(proposalsSchema, moveDiscussion=False)


class proposals(base.ATCTContent):
    """proposals of future projects"""
    implements(Iproposals)

    meta_type = "proposals"
    schema = proposalsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    


    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(proposals, PROJECTNAME)
