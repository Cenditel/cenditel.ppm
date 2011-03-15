"""Definition of the project content type
"""

from DateTime.DateTime import *

from zope.interface import implements

from Products.Archetypes import atapi

from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from Products.CMFCore.utils import getToolByName

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

from Products.validation.validators.RegexValidator import RegexValidator 
from Products.validation import validation

from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm.config import PROJECTNAME, TYPE_SUBFOLDER_PROJECT
from cenditel.ppm.interfaces import Iproject

projectSchema = folder.ATFolderSchema.copy() +  atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        name='manager',
        widget=atapi.SelectionWidget(
            label=_(u"Manager"),
            description=_(u"manager of project")
        ),
        schemata='Project',
        required=True,
        searchable=True,
        vocabulary_factory="cenditel.ppm.user",
    ),
    
    atapi.StringField( 
        name='status',
        widget=atapi.SelectionWidget( 
            format='select', 
            label=_(u"Status"),             
            description=_(u"State of the project"),           
        ),
        schemata='Project',
        vocabulary=[_(u"Time estimated"), _(u"Delayed"), _(u"Completed")] 
    ),

    atapi.DateTimeField(
        name='begin_date', 
        widget = atapi.CalendarWidget(
            format=('%Y;%m;%d;%H;%M'),  
            label=_(u'Begin Date'), 
        ),
        schemata='Project', 
        required=True, 
        validators = ('isValidDate'), 
    ), 

    atapi.DateTimeField(
        name='end_date',
        widget = atapi.CalendarWidget(
            format=('%Y;%m;%d;%H;%M'),
            label=_(u'End Date'),
        ),
        schemata='Project',
        required=True,
        validators = ('isValidDate'),
    ), 

    atapi.StringField(
        name='completed',
        schemata='Project',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"% Completed"),
            descrption=_(u"project % completed"),
        ),
    ),
    atapi.StringField(
        name='est_budget',
        schemata='Project',
        widget=atapi.StringWidget(
            label=_(u"Buget estimate"),
            descrption=_(u"Estimate Budget of the project"),
        ),
    ),

    atapi.StringField(
        name='act_budget',
        schemata='Project',
        widget=atapi.StringWidget(
            label=_(u"Actual Budget"),
            descrption=_(u"Actual Budget of the project"),
        ),
    ),

   atapi.StringField( 
        name='bud_status',
        schemata='Project', 
        widget=atapi.SelectionWidget( 
            format='select', 
            label=_(u"Budget Status"),
            description=_(u"Budget states of the project"),           
        ), 
        vocabulary=[_(u"On Budget"), _(u"Under Budget"), _(u"Over Budget")] 
    ), 

    atapi.StringField(
        name='assumptions',
        schemata='Project',
        widget=atapi.LinesWidget(
            label=_(u'Assumptions'),
            description=_(u'Assumptions of project'),
            size=5
        ) 
    ),

    atapi.StringField(
        name='tags',
        schemata='Project',
        searchable=True,
        widget=atapi.LinesWidget(
            label=_(u'Tags'),
            description=_(u'Tags of projects'),
            size=5
        )
    ),

    atapi.LinesField(
        name='suscribers',
        schemata='Project',
        widget=atapi.LinesWidget(
            label=_(u'Suscribers'),
            description=_(u'Suscribers of projects'),
            size=5
        )
    ),
	        
     DataGridField(
        name='project_folders',
        schemata='Project',
        widget=DataGridWidget(
            label=_(u"Project Folders"),
            description=_(u"Enter the names of sub-folders to create by default for each project created."),
            columns={
                     'title'   : Column('Title'),
                     'type'    : SelectColumn(_(u'Type'), vocabulary="getTypeSubFoldersProject"),
            },
        ),
        default=({'title' : _(u'Events'),         'type' : 'Event'},
                 {'title' : _(u'Documents'),      'type' : 'Folder'},
                 {'title' : _(u'Discussion'),     'type' : 'Ploneboard'},
                 {'title' : _(u'Forms'),          'type' : 'Folder'},
                 {'title' : _(u'Plans'),          'type' : 'Folder'},
                 {'title' : _(u'PoiTracker'),     'type' : 'PoiTracker'},
                 {'title' : _(u'Weblog'),         'type' : 'Weblog'},
        ),
        vocabulary_factory="cenditel.ppm.getLocalSubFolderVocabulary", #TODO verificar si existe
        required=True,
        columns=('title', 'type',),
     ),

))


# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

projectSchema['title'].storage = atapi.AnnotationStorage()
projectSchema['description'].storage = atapi.AnnotationStorage()
schemata.finalizeATCTSchema(
    projectSchema,
    folderish=True,
    moveDiscussion=False
)


class project(folder.ATFolder):
    """Create projects for a project portfolio"""

    implements(Iproject)

    meta_type = "project"
    schema = projectSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getTypeSubFoldersProject(self):
         return TYPE_SUBFOLDER_PROJECT

atapi.registerType(project, PROJECTNAME)
