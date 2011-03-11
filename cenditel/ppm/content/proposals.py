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

proposalsSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.TextField(
        name='templatest',
        widget=atapi.RichWidget(
            label=_(u"Summary"),
            description=_(u"template of the proposal"),
            rows="10",
        ),
        default='',
        storage=atapi.AnnotationStorage(),
        default_content_type = 'text/restructured',
        allowable_content_types=('text/plain', 'text/restructured', 'text/html',),
        default_output_type = 'text/x-html-safe',
        searchable=True,
        required=False
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
