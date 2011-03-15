from Products.validation.config import validation
try:
    from Products.validation.interfaces.IValidator import IValidator
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
    from interfaces.IValidator import IValidator
    del sys, os

from cenditel.ppm import ppmMessageFactory as _

ValidatorsList=[]

class GroupsValidator:
    """
       Validator for empty fields are not in groups within
       the portfolio of projects
    """

    __implements__ = IValidator

    def __init__(self,
        name,
        title='Groups validator',
        description='You will fail'):
            self.name = name
            self.title = title or name
            self.description = description

    def __call__(self, value, *args, **kwargs):
    	  Dic=value[0]
    	  value = str(value)
    	  if Dic['Title']=='':
    	      return (_(u'Group required, please correct.'))
       
ValidatorsList.append(GroupsValidator('isGroups', title='', description=''))

for validador in ValidatorsList:
         validation.register(validador)
