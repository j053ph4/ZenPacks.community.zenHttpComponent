from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

def addArgs(ob, context, data={}):
    ''' evaluate and return command line args '''
    parts = []
    if str(getattr(context, 'proxyAuth')) == "True" :
        parts.append('%s \"%s:%s\"' % (data['proxyAuth']['switch'],
                                       str(getattr(context, 'proxyAuthUser')),
                                       str(getattr(context, 'proxyAuthPassword'))
                                       ))
    
    if str(getattr(context, 'auth')) == "True" :
        parts.append('%s \"%s:%s\"' % (data['auth']['switch'],
                                       str(getattr(context, 'authUser')),
                                       str(getattr(context, 'authPassword'))
                                       ))
    parts.append("-t %s" % getattr(ob, "timeout"))
    return parts
    
def getUUID(ob):
    import uuid
    uid = uuid.uuid1()
    return str(uid)

HttpDefinition = type('HttpDefinition', (BasicDefinition,),  {
        'version' : Version(2, 1, 0),
        'zenpackroot' : "ZenPacks.community",
        'zenpackbase': "zenHttpComponent",
        'component' : 'HttpComponent',
        'componentData' : {
              'singular': 'Monitored URL',
              'plural': 'Monitored URLs',
              'displayed': 'eventComponent',
              'primaryKey': 'url',
              'properties': {
                            'hostname' : addProperty('Hostname (override)',default='id', switch='-H',override=True, isReference=True),
                            'ip' : addProperty('IP',default='manageIp', switch='-I',override=True, isReference=True),
                            'port' : addProperty('Port',default='80', switch='-p',optional=False),
                            'url' : addProperty('URL',default='/', switch='-u',optional=False),
                            'ssl': addProperty('SSL',default=False, ptype='boolean', switch='-S',optional=False),
                            'eventComponent' : addProperty('Alias',default='URL', optional=False),
                            'eventClass' : getEventClass('/WWW'),
                            'proxyAuth': addProperty('Proxy Authenticate',group='Authentication', default=False, ptype='boolean', switch='-b'),
                            'proxyAuthUser' : addProperty('Proxy User',group='Authentication'),
                            'proxyAuthPassword' : addProperty('Proxy Password',group='Authentication',ptype='password'),
                            'auth': addProperty('Authenticate',group='Authentication', default=False, ptype='boolean', switch='-a'),
                            'authUser' : addProperty('User',group='Authentication'),
                            'authPassword' : addProperty('Password',group='Authentication',ptype='password'),
                            'regex' : addProperty('Case Sensitive REGEX',group='Content', switch='-r'),
                            'eregex' : addProperty('Case Insensitive REGEX ',group='Content', switch='-R'),
                            'expect' : addProperty('Expect (comma-delimited strings)',group='Content', switch='-e'),
                            'string' : addProperty('Find string',group='Content', switch='-s'),
                            'invert' :  addProperty('Invert Match',group='Content',default=False, ptype='boolean', switch='--invert-regex'),
                            'post' : addProperty('POST',group='Content', switch='-P'),
                            'contentType' : addProperty('Content Type', group='Content', switch='-T'),
                            'method': addProperty('HTTP method',group='Miscellaneous', switch='-j'),
                            'cert': addProperty('Certificate',group='Miscellaneous',default=None, ptype='int', switch='-C'),
                            'nobody': addProperty('Headers Only',group='Miscellaneous', default=False, ptype='boolean', switch='-N'),
                            'maxage' : addProperty('Max Age',group='Miscellaneous', switch='-M'),
                            'onRedirect' : addProperty('Redirect Behavior', group='Miscellaneous',default='follow', switch='-f'),
                            'urlize' :  addProperty('Output Link',group='Miscellaneous', default=False, ptype='boolean', switch='-L'),
                            },
              },
        'componentMethods': [getUUID],
        'cmdFile':'check_http',
        'addManual' : True,
        'createDS' : True,
        'ignoreKeys' : ['auth', 'authUser', 'authPassword','proxyAuth', 'proxyAuthUser', 'proxyAuthPassword','getEventClasses', 'getIpserviceLink'],
        'datasourceMethods' : [addArgs],
        'datapoints' : ['size','time'],
        }
)

addDefinitionDeviceComponentRelation(HttpDefinition,'manageIp', 'ip',
                          'httpcomponents', ToMany, 'ZenPacks.community.HttpDefinition.HttpComponent','port',
                          'ipservice',  ToOne, 'Products.ZenModel.IpService', 'port',
                          'IP Service', 'port')
