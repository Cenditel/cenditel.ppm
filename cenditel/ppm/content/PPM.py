"""Definition of the PPM content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata


from cenditel.ppm import CenditelPpmMF as _
from cenditel.ppm.config import PROJECTNAME
from cenditel.ppm.interfaces import IPPM
#from cenditel.ppm.validator import GroupsValidator

PPMSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-


))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

PPMSchema['title'].storage = atapi.AnnotationStorage()
PPMSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    PPMSchema,
    folderish=True,
    moveDiscussion=False
)

class PPM(folder.ATFolder):
    """A Folder dedicate to proposals and projects"""
    implements(IPPM)

    meta_type = "PPM"
    schema = PPMSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(PPM, PROJECTNAME)
