"""Common configuration constants
"""

from Products.Archetypes.utils import DisplayList

from cenditel.ppm import ppmMessageFactory as _

PROJECTNAME = 'cenditel.ppm'

ADD_PERMISSIONS = {
    'folderproj': 'cenditel.ppm: Add folderproj',
    'proposals': 'cenditel.ppm: Add proposals',
    'project': 'cenditel.ppm: Add project',
}

TYPE_SUBFOLDER_PROJECT = DisplayList((
    ("Events", _(u"Events/Activities")),
    ("Folder", _(u"Folder")),
    ("Ploneboard", _(u"Discussions board")),
    ("PoiTracker", _(u"Demands")),
    ("Weblog", _(u"Blog")),
    ))
