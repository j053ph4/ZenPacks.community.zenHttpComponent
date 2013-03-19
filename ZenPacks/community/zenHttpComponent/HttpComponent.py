from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import *

'''
args:  classname,classname,properties,_properties,relname,sortkey,viewname
'''

class HttpComponent(OSComponent, ManagedEntity, ZenPackPersistence):
    '''
    	basic Component class
    '''
    
    portal_type = meta_type = 'HttpComponent'
    
    ip = ''
    expect = None
    proxyAuthUser = None
    authPassword = None
    regex = None
    urlize = False
    invert = False
    hostname = ''
    maxage = None
    port = '80'
    proxyAuthPassword = None
    method = None
    authUser = None
    contentType = None
    string = None
    nobody = False
    auth = False
    ssl = False
    eventComponent = 'URL'
    post = None
    eregex = None
    onRedirect = 'follow'
    url = '/'
    cert = False
    proxyAuth = False
    eventKey = '/WWW'

    _properties = (
    {'id': 'ip', 'type': 'string','mode': '', 'switch': '-I' },
    {'id': 'expect', 'type': 'string','mode': '', 'switch': '-e' },
    {'id': 'proxyAuthUser', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'authPassword', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'regex', 'type': 'string','mode': '', 'switch': '-r' },
    {'id': 'urlize', 'type': 'boolean','mode': '', 'switch': '-L' },
    {'id': 'invert', 'type': 'boolean','mode': '', 'switch': '--invert-regex' },
    {'id': 'hostname', 'type': 'string','mode': '', 'switch': '-H' },
    {'id': 'maxage', 'type': 'string','mode': '', 'switch': '-M' },
    {'id': 'port', 'type': 'string','mode': '', 'switch': '-p' },
    {'id': 'proxyAuthPassword', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'method', 'type': 'string','mode': '', 'switch': '-j' },
    {'id': 'authUser', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'contentType', 'type': 'string','mode': '', 'switch': '-T' },
    {'id': 'string', 'type': 'string','mode': '', 'switch': '-s' },
    {'id': 'nobody', 'type': 'boolean','mode': '', 'switch': '-N' },
    {'id': 'auth', 'type': 'boolean','mode': '', 'switch': '-a' },
    {'id': 'ssl', 'type': 'boolean','mode': '', 'switch': '-S' },
    {'id': 'eventComponent', 'type': 'string','mode': '', 'switch': 'None' },
    {'id': 'post', 'type': 'string','mode': '', 'switch': '-P' },
    {'id': 'eregex', 'type': 'string','mode': '', 'switch': '-R' },
    {'id': 'onRedirect', 'type': 'string','mode': '', 'switch': '-f' },
    {'id': 'url', 'type': 'string','mode': '', 'switch': '-u' },
    {'id': 'cert', 'type': 'boolean','mode': '', 'switch': '-C' },
    {'id': 'proxyAuth', 'type': 'boolean','mode': '', 'switch': '-b' },
    {'id': 'eventKey', 'type': 'string','mode': '', 'switch': 'None' },

    )
    
    _relations = OSComponent._relations + (
        ('os', ToOne(ToManyCont, 'Products.ZenModel.OperatingSystem', 'httpComponents')),
        )

    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
        
    def statusMap(self):
        self.status = 0
        return self.status
    
    def getStatus(self):
        return self.statusMap()
    
    def primarySortKey(self):
        return self.url
    
    def viewName(self):
        return self.eventComponent
    
    name = titleOrId = viewName


