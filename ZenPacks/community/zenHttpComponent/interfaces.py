
'''
args: componentInterface,comopnentInterfaceproperties,componentIFacade,iFacadeMethodName
'''

from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version
if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IHttpComponentInfo(IComponentInfo):
    ip = SingleLineText(title=_t(u'IP'))
    expect = SingleLineText(title=_t(u'Expect (comma-delimited strings)'))
    proxyAuthUser = SingleLineText(title=_t(u'Proxy User'))
    authPassword = schema.Password(title=_t(u'Password'))
    regex = SingleLineText(title=_t(u'Regex (Case sensitive)'))
    urlize = schema.Bool(title=_t(u'Output Link'))
    invert = schema.Bool(title=_t(u'Invert Match'))
    hostname = SingleLineText(title=_t(u'Hostname (override)'))
    maxage = SingleLineText(title=_t(u'Max Age'))
    port = SingleLineText(title=_t(u'Port'))
    proxyAuthPassword = schema.Password(title=_t(u'Proxy Password'))
    method = SingleLineText(title=_t(u'HTTP method'))
    authUser = SingleLineText(title=_t(u'User'))
    contentType = SingleLineText(title=_t(u'Content Type'))
    string = SingleLineText(title=_t(u'Find string'))
    nobody = schema.Bool(title=_t(u'Headers Only'))
    auth = schema.Bool(title=_t(u'Authenticate'))
    ssl = schema.Bool(title=_t(u'SSL'))
    eventComponent = SingleLineText(title=_t(u'Alias'))
    post = SingleLineText(title=_t(u'POST'))
    eregex = SingleLineText(title=_t(u'Regex (Case insensitive)'))
    onRedirect = SingleLineText(title=_t(u'Redirect Behavior'))
    url = SingleLineText(title=_t(u'URL'))
    cert = schema.Bool(title=_t(u'Certificate'))
    proxyAuth = schema.Bool(title=_t(u'Proxy Authenticate'))
    eventKey = SingleLineText(title=_t(u'Event Key'))



class IzenHttpComponentFacade(IFacade):
    def addHttpComponent(self, ob, **kwargs):
        ''''''

'''
args : dsinterface,dsinterfaceproperties
'''

# datasource interface
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

if Version.parse('Zenoss ' + ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine

class IHttpComponentDataSourceInfo(IRRDDataSourceInfo):
    authUser = SingleLineText(title=_t(u'User'))
    contentType = SingleLineText(title=_t(u'Content Type'))
    string = SingleLineText(title=_t(u'Find string'))
    ip = SingleLineText(title=_t(u'IP'))
    nobody = schema.Bool(title=_t(u'Headers Only'))
    auth = schema.Bool(title=_t(u'Authenticate'))
    ssl = schema.Bool(title=_t(u'SSL'))
    eventComponent = SingleLineText(title=_t(u'Alias'))
    expect = SingleLineText(title=_t(u'Expect (comma-delimited strings)'))
    proxyAuthUser = SingleLineText(title=_t(u'Proxy User'))
    cycletime = schema.Int(title=_t(u'Cycle Time (s)'))
    post = SingleLineText(title=_t(u'POST'))
    eregex = SingleLineText(title=_t(u'Regex (Case insensitive)'))
    authPassword = schema.Password(title=_t(u'Password'))
    regex = SingleLineText(title=_t(u'Regex (Case sensitive)'))
    urlize = schema.Bool(title=_t(u'Output Link'))
    url = SingleLineText(title=_t(u'URL'))
    invert = schema.Bool(title=_t(u'Invert Match'))
    hostname = SingleLineText(title=_t(u'Hostname (override)'))
    maxage = SingleLineText(title=_t(u'Max Age'))
    port = SingleLineText(title=_t(u'Port'))
    proxyAuthPassword = schema.Password(title=_t(u'Proxy Password'))
    cert = schema.Bool(title=_t(u'Certificate'))
    proxyAuth = schema.Bool(title=_t(u'Proxy Authenticate'))
    eventKey = SingleLineText(title=_t(u'Event Key'))
    timeout = SingleLineText(title=_t(u'Timeout (s)'))
    method = SingleLineText(title=_t(u'HTTP method'))
    onRedirect = SingleLineText(title=_t(u'Redirect Behavior'))


