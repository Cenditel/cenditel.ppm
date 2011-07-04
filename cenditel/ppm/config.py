"""Common configuration constants
"""

from Products.Archetypes.utils import DisplayList

from cenditel.ppm import ppmMessageFactory as _


PROJECTNAME = 'cenditel.ppm'

ADD_PERMISSIONS = {
    'PPM': 'cenditel.ppm: Add PPM',
    'proposals': 'cenditel.ppm: Add proposals',
    'Project': 'cenditel.ppm: Add Project',
}

TYPE_SUBFOLDER_PROJECT = DisplayList((
    ("Event", _(u"Events/Activities")),
    ("Folder", _(u"Folder")),
    ("Ploneboard", _(u"Discussions board")),
    ("PoiTracker", _(u"Demands")),
    ("Weblog", _(u"Blog")),
    ))

SCHEDULE_STATUS_PROJECT = DisplayList((
    ("est", _(u"Estimated")), # none
    ("comm", _(u"Committed")), # none
    ("plan", _(u"In Planning")), # yellow
    ("hold", _(u"On Hold")), # none
    ("ipa", _(u"In Process - Ahead of Schedule")), # green
    ("ipb", _(u"In Process - Begin Schedule")), # red
    ("ipo", _(u"In Process - On Schedule")), # green
    ("comp", _(u"Completed")), # none
    ))

BUDGET_STATUS_PROJECT = DisplayList((
    ("onbud", _(u"On Budget")), # green
    ("underb", _(u"Under Budget")), # green
    ("overb", _(u"Over Budget")), # red
    ("pend", _(u"Pending")), # yellow
    ))

PROPOSAL_RATINGS_SCHEME = DisplayList((
    ("1", _(u"1: No Ratings")), # white
    ("1.0", _(u"1.0: All Low Ratings")), # #6F8000
    ("1.5", _(u"1.5: Many Low Ratings")), # #6F9800
    ("2.0", _(u"2.0: Low Ratings")), # #6FA000
    ("2.5", _(u"2.5: Below Average Ratings")), # #6FB000
    ("3.0", _(u"3.0: Average Ratings")), # #6FC800
    ("3.5", _(u"3.5: Above Average Ratings")), # #6FD000
    ("4.0", _(u"4.0: High Ratings")), # #6FE000
    ("4.5", _(u"4.5: Many High Ratings")), # #6FEF00
    ("5.0", _(u"5.0: All High Ratings")), # #6FFF00
    ))

PROPOSAL_RATINGS_COLOR_SCHEME = DisplayList((
    ("1", "white"), # 
    ("1.0", "#6F8000"), # 
    ("1.5", "#6F9800"), # 
    ("2.0", "#6FA000"), # 
    ("2.5", "#6FB000"), # 
    ("3.0", "#6FC800"), # 
    ("3.5", "#6FD000"), # 
    ("4.0", "#6FE000"), # 
    ("4.5", "#6FEF00"), # 
    ("5.0", "#6FFF00"), # 
    ))
    
PRODUCT_DEPENDENCIES = (
    "CMFPlacefulWorkflow",
    "Quills",
    "AddRemoveWidget",
    "DataGridField",
    "Poi",
    "Ploneboard",
    "Calendaring",
    "collective.calendarwidget",
    "Products.FCKeditor",
    "CPFCKTemplates",
     )
     
