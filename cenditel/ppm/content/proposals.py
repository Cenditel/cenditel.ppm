"""Definition of the proposals content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.Archetypes.utils import Message

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm.config import PROJECTNAME
from cenditel.ppm.interfaces import Iproposals
from cenditel.ppm.validator import GroupsValidator
from Products.DataGridField import DataGridField, DataGridWidget

proposalsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

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
    
    
    atapi.TextField(
        name='templatest',
        allowable_content_types=('text/html',),
        widget=atapi.RichWidget(
            label=_(u"Summary"),
            description=_(u"Proposal summary of a future project"),
        ),
        default_content_type="text/html",
        default_output_type="text/html",
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

proposalsSchema['title'].storage = atapi.AnnotationStorage()
proposalsSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(proposalsSchema, moveDiscussion=False)


class proposals(base.ATCTContent):
    """Create proposals of future projects for a project portfolio"""

    implements(Iproposals)

    meta_type = "proposals"
    schema = proposalsSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    
atapi.registerType(proposals, PROJECTNAME)
