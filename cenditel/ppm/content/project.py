"""Definition of the project content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from cenditel.ppm import ppmMessageFactory as _
from cenditel.ppm.interfaces import Iproject
from cenditel.ppm.config import PROJECTNAME
from DateTime.DateTime import *
from Products.validation.validators.RegexValidator import RegexValidator 
from Products.validation import validation 
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.atapi import LinesWidget
#from cenditel.ppm.usuarios import Usuarios
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn

from Products.Archetypes.utils import DisplayList




projectSchema = folder.ATFolderSchema.copy() +  atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
    name='manager',
    schemata='Project',
	required=True,
	searchable=True,
	#storage=atapi.AnnotationStorage(),
    vocabulary_factory="cenditel.ppm.user",
    #vocabulary_display_path_bound=-1, # Avoid silly Archetypes object title magic
    #enforceVocabulary=True,
	widget=atapi.SelectionWidget(
            label=_(u"Manager"),
	    description=_(u"manager of project")
        ),
    ),


   atapi.StringField( 
        name='status', 
        schemata='Project',
        widget=atapi.SelectionWidget( 
            format='select', 
            label=_(u"Status"),             
           description=_(u"State of the project"),           
        ), 
        vocabulary=[_(u"Time estimated"), _(u"Delayed"), _(u"Completed")] 
    ), 

    atapi.DateTimeField('begin_date', 
                schemata='Project',
                required=True,
	            #required=True,
                validators = ('isValidDate'), 
                widget = atapi.CalendarWidget(format=('%Y;%m;%d;%H;%M'), 
                label=_(u'Begin Date'),) 
                ), 

    atapi.DateTimeField(
                name='end_date',
                schemata='Project',
                required=True,
	            #required=True,
                validators = ('isValidDate'), 
                widget = atapi.CalendarWidget(format=('%Y;%m;%d;%H;%M'), 
                label=_(u'End Date'),) 
                ), 

    atapi.StringField('completed',
    schemata='Project',
	storage=atapi.AnnotationStorage(),
	widget=atapi.StringWidget(
            label=_(u"% Completed"),
	    descrption=_(u"project % completed")
        ),
    ),
    atapi.StringField('est_budget',
    schemata='Project',
	#storage=atapi.AnnotationStorage(),
	widget=atapi.StringWidget(
            label=_(u"Buget estimate"),
	    descrption=_(u"Estimate Budget of the project")
        ),
    ),

    atapi.StringField(
        name='act_budget',
        schemata='Project',
	    #storage=atapi.AnnotationStorage(),
	    widget=atapi.StringWidget(
            label=_(u"Actual Budget"),
	        descrption=_(u"Actual Budget of the project")
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

    atapi.StringField('assumptions',
    schemata='Project',
	widget=atapi.LinesWidget(
            label=_(u'Assumptions'),
            description=_(u'Assumptions of project'),
	    size=5)
    ),

    atapi.StringField('tags',
    schemata='Project',
	searchable=True,
	widget=atapi.LinesWidget(
            label=_(u'Tags'),
            description=_(u'Tags of projects'),
	    size=5)
    ),

    atapi.LinesField('suscribers',
    schemata='Project',
	widget=atapi.LinesWidget(
            label=_(u'Suscribers'),
	    description=_(u'Suscribers of projects'),
	    size=5)
    ),
	        
     DataGridField(
            name='project_folders',
            schemata='Project',
            vocabulary_factory="cenditel.ppm.getLocalSubFolderVocabulary",
            default=({'title' : _(u'Events'),         'type' : 'Folder'},
                     {'title' : _(u'Documents'),      'type' : 'Folder'},
                     {'title' : _(u'Discussion'),     'type' : 'Ploneboard'},
                     {'title' : _(u'Forms'),          'type' : 'Folder'},
                     {'title' : _(u'Plans'),          'type' : 'Folder'},
                     {'title' : _(u'PoiTracker'),     'type' : 'PoiTracker'},
                     {'title' : _(u'Weblog'),         'type' : 'Weblog'},
                    ),
            widget=DataGridWidget(
                label=_(u"Project Folders"),
                description=_(u"Enter the names of sub-folders to create by default for each project created."),
                columns={
                        'title'   : Column('Title'),
                        'type'    : SelectColumn('Type', vocabulary="getSampleVocabulary"),
               
                    },
                label_msgid='ppm_label_proj_folders',
                description_msgid='ppm_help_proj_folders',
                i18n_domain='PPM',
            ),
            required=True,
            columns=('title', _(u'type'),),
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
    
    def getSampleVocabulary(self):
         return DisplayList(
         (("Folder", "Folder",),
         ("Ploneboard", "Ploneboard",),
         ("PoiTracker", "PoiTracker",),
         ("Weblog", "Weblog",),))

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
   # def subfolders (obj):
   # obj = getattr(projectSchema)
   # projectSchema.invokeFactory(id='subfolder1', type_name='Folder')
   # return obj


atapi.registerType(project, PROJECTNAME)
