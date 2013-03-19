from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenHttpComponent.interfaces import *

'''
args:  zenpack,compInfo,compInterface,infoProperties
'''

class HttpComponentInfo(ComponentInfo):
    implements( IHttpComponentInfo )
    ip = ProxyProperty('ip')
    expect = ProxyProperty('expect')
    proxyAuthUser = ProxyProperty('proxyAuthUser')
    authPassword = ProxyProperty('authPassword')
    regex = ProxyProperty('regex')
    urlize = ProxyProperty('urlize')
    invert = ProxyProperty('invert')
    hostname = ProxyProperty('hostname')
    maxage = ProxyProperty('maxage')
    port = ProxyProperty('port')
    proxyAuthPassword = ProxyProperty('proxyAuthPassword')
    method = ProxyProperty('method')
    authUser = ProxyProperty('authUser')
    contentType = ProxyProperty('contentType')
    string = ProxyProperty('string')
    nobody = ProxyProperty('nobody')
    auth = ProxyProperty('auth')
    ssl = ProxyProperty('ssl')
    eventComponent = ProxyProperty('eventComponent')
    post = ProxyProperty('post')
    eregex = ProxyProperty('eregex')
    onRedirect = ProxyProperty('onRedirect')
    url = ProxyProperty('url')
    cert = ProxyProperty('cert')
    proxyAuth = ProxyProperty('proxyAuth')
    eventKey = ProxyProperty('eventKey')


'''
args : zenpackname,zenpackname,dsclass,dsvolcclass,dsvolcvar,dsinfo,dsinterface,dsinfoproperties
'''
# datasource info
from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from zope.schema.vocabulary import SimpleVocabulary
from Products.Zuul.infos.template import RRDDataSourceInfo
from ZenPacks.community.zenHttpComponent.interfaces import *
from ZenPacks.community.zenHttpComponent.datasources.HttpComponentDataSource import *

def HttpComponentRedirectVocabulary(context):
    return SimpleVocabulary.fromValues(HttpComponentDataSource.onRedirectOptions)

class HttpComponentDataSourceInfo(RRDDataSourceInfo):
    implements(IHttpComponentDataSourceInfo)
    authUser = ProxyProperty('authUser')
    contentType = ProxyProperty('contentType')
    string = ProxyProperty('string')
    ip = ProxyProperty('ip')
    nobody = ProxyProperty('nobody')
    auth = ProxyProperty('auth')
    ssl = ProxyProperty('ssl')
    eventComponent = ProxyProperty('eventComponent')
    expect = ProxyProperty('expect')
    proxyAuthUser = ProxyProperty('proxyAuthUser')
    cycletime = ProxyProperty('cycletime')
    post = ProxyProperty('post')
    eregex = ProxyProperty('eregex')
    authPassword = ProxyProperty('authPassword')
    regex = ProxyProperty('regex')
    urlize = ProxyProperty('urlize')
    url = ProxyProperty('url')
    invert = ProxyProperty('invert')
    hostname = ProxyProperty('hostname')
    maxage = ProxyProperty('maxage')
    port = ProxyProperty('port')
    proxyAuthPassword = ProxyProperty('proxyAuthPassword')
    cert = ProxyProperty('cert')
    proxyAuth = ProxyProperty('proxyAuth')
    eventKey = ProxyProperty('eventKey')
    timeout = ProxyProperty('timeout')
    method = ProxyProperty('method')
    onRedirect = ProxyProperty('onRedirect')

    @property
    def testable(self):
        ''''''
        return False

