from ZPublisher.HTTPRequest import FileUpload
from Globals import package_home
import os

GLOBALS=globals()
PACKAGE_HOME=package_home(GLOBALS)
GIF = open(os.path.join(PACKAGE_HOME, 'tool.gif')).read()
TEXT='file data'

class File(FileUpload):
    __allow_access_to_unprotected_subobjects__ = 1
    filename = 'dummy.txt'
    data = TEXT
    headers = {}

    def __init__(self, filename=None, data=None, headers=None):
        if filename is not None:
            self.filename = filename
        if data is not None:
            self.data = data
        if headers is not None:
            self.headers = headers

    def seek(self, *args): pass
    def tell(self, *args): return 1
    def read(self, *args): return self.data


class DefaultImage(File):
    filename = 'default.gif'
    data = GIF
