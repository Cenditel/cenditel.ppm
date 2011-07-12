"""Definition of the Project content type
"""

from DateTime.DateTime import *

from zope.interface import implements, classImplements

from Products.Archetypes import atapi

from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content import base

from Products.CMFCore.utils import getToolByName

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

from Products.validation import validation
from Products.validation.validators.RegexValidator import RegexValidator
from Products.Archetypes.interfaces import IMultiPageSchema
from Products.Archetypes.atapi import InAndOutWidget
from Products.AddRemoveWidget import AddRemoveWidget
from Products.FCKeditor.FckWidget import FckWidget
from collective.calendarwidget.widget import CalendarWidget

from cenditel.ppm import CenditelPpmMF as _
from cenditel.ppm.config import PROJECTNAME, TYPE_SUBFOLDER_PROJECT, SCHEDULE_STATUS_PROJECT, BUDGET_STATUS_PROJECT
from cenditel.ppm.interfaces import IProject
from cenditel.ppm.validator import SuscriberValidator
#from cenditel.ppm.validator import UsersValidator

projectSchema = folder.ATFolderSchema.copy() +  atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.LinesField(
        name='manager',
        required=True,
        searchable=True,
        storage = atapi.AnnotationStorage(),
        vocabulary_factory="cenditel.ppm.user",
        widget=InAndOutWidget(
            size = 10,
            label=_(u"Manager"),
            description=_(u"Project Manager"),
        ),
        #schemata='Project',
        
    ),
    
    atapi.StringField( 
        name='status',
        widget=atapi.SelectionWidget( 
            format='select', 
            label=_(u"Status"),
            description=_(u"Project Status"),
        ),
        vocabulary=SCHEDULE_STATUS_PROJECT,
        schemata='Project',
    ),

    atapi.DateTimeField(
        name='begin_date', 
        widget=CalendarWidget(
            #format=('%d.%m.%Y.%H.%M'),  
            label=_(u'Begin Date'),
            description=_(u"Project Begin Date"),
        ),
        validators = ('isValidDate'),
        required=True, 
        #schemata='Project',
         
    ), 

    atapi.DateTimeField(
        name='end_date',
        widget=CalendarWidget(
            #format=('%Y;%m;%d;%H;%M'),
            label=_(u'End Date'),
            description=_(u"Project End Date"),
        ),
        validators = ('isValidDate'),
        required=True,
        #schemata='Project',
        
    ), 

    atapi.StringField(
        name='completed',
        widget=atapi.StringWidget(
            label=_(u"% Completed"),
            description=_(u"Project % completed"),
        ),
        
        storage=atapi.AnnotationStorage(),
        schemata='Project',
    ),
    atapi.StringField(
        name='est_budget',
        widget=atapi.StringWidget(
            label=_(u"Estimated Budget"),
            description=_(u"Project Estimated Budget"),
        ),
        schemata='Project',
    ),

    atapi.StringField(
        name='act_budget',
        widget=atapi.StringWidget(
            label=_(u"Actual Budget"),
            description=_(u"Project Actual Budget"),
        ),
        schemata='Project',
    ),

   atapi.StringField( 
        name='bud_status',
        widget=atapi.SelectionWidget( 
            format='select', 
            label=_(u"Budget Status"),
            description=_(u"Project Status Budget"),           
        ),
        vocabulary=BUDGET_STATUS_PROJECT,
        schemata='Project',
    ), 

    atapi.TextField(
        name='assumptions',
        widget=FckWidget(
            label=_(u'Assumptions'),
            description=_(u'Project Assumptions'),
            allow_file_upload=False,
            rows=5,
            cols=40,
        ),
        validators=('isTidyHtmlWithCleanup',),
        allowable_content_types=('text/html',),
        default_content_type="text/html",
        default_output_type="text/x-html-safe", 
        storage=atapi.AnnotationStorage(),
        
        searchable=True,
        required=False,
        schemata='Project',
    ),

    atapi.StringField(
        name='tags',
        widget=atapi.LinesWidget(
            label=_(u'Tags'),
            description=_(u'Project Tags'),
            size=5
        ),  
        searchable=True,
        schemata='Project',
    ),

    atapi.LinesField(
        name='suscribers',
        widget=atapi.LinesWidget(
#        widget=atapi.StringWidget(
            label=_(u'Suscribers'),
            description=_(u"Enter every email address for the suscribers of projects, please everyone preceded by prefix 'mailto:'"),
            size=5,
        ),
        validators=('areSuscribers',),
        #schemata='Project',
         
    ),
	        
     DataGridField(
        name='project_folders',
        widget=DataGridWidget(
            label=_(u"Project Folders"),
            description=_(u"Enter the names of sub-folders to create by default for each project created."),
            columns={
                     'title'   : Column('Title'),
                     'type'    : SelectColumn(_(u'Type'), vocabulary="getTypeSubFoldersProject"),
            },
        ),
        columns=('title', 'type',),
        default=({'title' : _(u'Events'),         'type' : 'Folder'},
                 {'title' : _(u'Documents'),      'type' : 'Folder'},
                 {'title' : _(u'Discussions'),    'type' : 'Ploneboard'},
                 {'title' : _(u'Forms'),          'type' : 'Folder'},
                 {'title' : _(u'Plans'),          'type' : 'Folder'},
                 {'title' : _(u'Demands'),        'type' : 'PoiTracker'},
                 {'title' : _(u'Weblog'),         'type' : 'Weblog'},
        ),
        schemata='Project',
        required=True,
        vocabulary_factory="cenditel.ppm.getLocalSubFolderVocabulary", #TODO verificar si existe
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


class Project(folder.ATFolder):
    """Create projects for a project portfolio"""

    #implements(IProject)
    implements(IProject, IMultiPageSchema)
    meta_type = "Project"
    schema = projectSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

    def getTypeSubFoldersProject(self):
         return TYPE_SUBFOLDER_PROJECT


atapi.registerType(Project, PROJECTNAME)
