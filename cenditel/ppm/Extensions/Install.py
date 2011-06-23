import transaction
from StringIO import StringIO
from Products.CMFCore.utils import getToolByName
from cenditel.ppm.config import PRODUCT_DEPENDENCIES


EXTENSION_PROFILES = ('cenditel.ppm:default',)

def install(self,reinstall=False):
    
    
    """Install a set of products (which themselves may either use Install.py
    or GenericSetup extension profiles for their configuration) and then
    install a set of extension profiles.
    
    One of the extension profiles we install is that of this product. This
    works because an Install.py installation script (such as this one) takes
    precedence over extension profiles for the same product in 
    portal_quickinstaller. 
    
    We do this because it is not possible to install other products during
    the execution of an extension profile (i.e. we cannot do this during
    the importVarious step for this profile).
    """
    
    portal_quickinstaller = getToolByName(self, 'portal_quickinstaller')
    portal_setup = getToolByName(self, 'portal_setup')
    from Products.GenericSetup.context import Logger,SetupEnviron
    import logging
    obj = SetupEnviron()
    out = StringIO()
    logger = obj.getLogger("cenditel.ppm")
    outch = logging.StreamHandler(out)
    logger.addHandler(outch)
    #import pdb; pdb.set_trace()
    if reinstall:
        for product in PRODUCT_DEPENDENCIES:
            
            if not portal_quickinstaller.isProductInstalled(product):
                portal_quickinstaller.installProduct(product)
                transaction.savepoint()
        for product in PRODUCT_DEPENDENCIES:
            #import pdb; pdb.set_trace()
            if portal_quickinstaller.isProductInstalled(product):
                portal_quickinstaller.reinstallProducts([product])
                transaction.savepoint()
            elif not portal_quickinstaller.isProductInstalled(product):
                portal_quickinstaller.installProduct(product)
                transaction.savepoint()
    else:
        for product in PRODUCT_DEPENDENCIES:
            if not portal_quickinstaller.isProductInstalled(product):
               logger.info("Installing missing product: %s" % product)
               portal_quickinstaller.installProduct(product)
               transaction.savepoint()
               
    for extension_id in EXTENSION_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id, purge_old=False)
        product_name = extension_id.split(':')[0]
        portal_quickinstaller.notifyInstalled(product_name)
        transaction.savepoint()
