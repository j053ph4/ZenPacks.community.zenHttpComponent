from Products.ZenModel.RRDDataSource import RRDDataSource
from Products.ZenModel.ZenPackPersistence import ZenPackPersistence
from AccessControl import ClassSecurityInfo, Permissions
from Products.ZenUtils.ZenTales import talesCompile, getEngine
from Products.ZenUtils.Utils import binPath

'''
Args:  classname, datasourcename, zenpackname, eventClass, cycletime, timeout, cmdfile, dpoints, properties,_properties,datasourcename,datasourcename
'''

class HttpComponentDataSource(ZenPackPersistence, RRDDataSource):
    DATASOURCE = 'HttpComponent'
    ZENPACKID = 'ZenPacks.community.zenHttpComponent'
    sourcetypes = (DATASOURCE,)
    sourcetype = DATASOURCE
    eventClass = '/WWW'
    cycletime = 60
    timeout = 300
    component = '${here/eventComponent}'
    cmdFile = 'check_http'
    provided = False
    dpoints = ['size', 'time']
    
    authUser = '${here/authUser}'
    contentType = '${here/contentType}'
    string = '${here/string}'
    ip = '${here/ip}'
    nobody = '${here/nobody}'
    auth = '${here/auth}'
    ssl = '${here/ssl}'
    eventComponent = '${here/eventComponent}'
    expect = '${here/expect}'
    proxyAuthUser = '${here/proxyAuthUser}'
    post = '${here/post}'
    eregex = '${here/eregex}'
    authPassword = '${here/authPassword}'
    regex = '${here/regex}'
    urlize = '${here/urlize}'
    url = '${here/url}'
    invert = '${here/invert}'
    hostname = '${here/hostname}'
    maxage = '${here/maxage}'
    port = '${here/port}'
    proxyAuthPassword = '${here/proxyAuthPassword}'
    cert = '${here/cert}'
    proxyAuth = '${here/proxyAuth}'
    eventKey = '${here/eventKey}'
    method = '${here/method}'
    onRedirect = '${here/onRedirect}'

    _properties = RRDDataSource._properties + (
    {'id': 'authUser', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'contentType', 'type': 'string','mode': 'w', 'switch': '-T'},
    {'id': 'string', 'type': 'string','mode': 'w', 'switch': '-s'},
    {'id': 'ip', 'type': 'string','mode': 'w', 'switch': '-I'},
    {'id': 'nobody', 'type': 'boolean','mode': 'w', 'switch': '-N'},
    {'id': 'auth', 'type': 'boolean','mode': 'w', 'switch': '-a'},
    {'id': 'ssl', 'type': 'boolean','mode': 'w', 'switch': '-S'},
    {'id': 'eventComponent', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'expect', 'type': 'string','mode': 'w', 'switch': '-e'},
    {'id': 'proxyAuthUser', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'cycletime', 'type': 'int','mode': 'w', 'switch': 'None'},
    {'id': 'post', 'type': 'string','mode': 'w', 'switch': '-P'},
    {'id': 'eregex', 'type': 'string','mode': 'w', 'switch': '-R'},
    {'id': 'authPassword', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'regex', 'type': 'string','mode': 'w', 'switch': '-r'},
    {'id': 'urlize', 'type': 'boolean','mode': 'w', 'switch': '-L'},
    {'id': 'url', 'type': 'string','mode': 'w', 'switch': '-u'},
    {'id': 'invert', 'type': 'boolean','mode': 'w', 'switch': '--invert-regex'},
    {'id': 'hostname', 'type': 'string','mode': 'w', 'switch': '-H'},
    {'id': 'maxage', 'type': 'string','mode': 'w', 'switch': '-M'},
    {'id': 'port', 'type': 'string','mode': 'w', 'switch': '-p'},
    {'id': 'proxyAuthPassword', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'cert', 'type': 'boolean','mode': 'w', 'switch': '-C'},
    {'id': 'proxyAuth', 'type': 'boolean','mode': 'w', 'switch': '-b'},
    {'id': 'eventKey', 'type': 'string','mode': 'w', 'switch': 'None'},
    {'id': 'timeout', 'type': 'string','mode': 'w', 'switch': '-t'},
    {'id': 'method', 'type': 'string','mode': 'w', 'switch': '-j'},
    {'id': 'onRedirect', 'type': 'string','mode': 'w', 'switch': '-f'},

    )
    
    _relations = RRDDataSource._relations + (
        )
        
    factory_type_information = (
    {
        'immediate_view' : 'editHttpComponentDataSource',
        'actions'        :
        (
            { 'id'            : 'edit',
              'name'          : 'Data Source',
              'action'        : 'editHttpComponentDataSource',
              'permissions'   : ( Permissions.view, ),
            },
        )
    },
    )

    security = ClassSecurityInfo()

    def __init__(self, id, title=None, buildRelations=True):
        RRDDataSource.__init__(self, id, title, buildRelations)
        self.addDataPoints()
    
    def getDescription(self):
        if self.sourcetype == self.DATASOURCE:
            return self.component
        return RRDDataSource.getDescription(self)
    
    def useZenCommand(self):
        return True
        
    def getCommand(self, context):
        '''
            generate the plugin command
        '''
        cmd = binPath(self.cmdFile)
        if self.provided == False:
            cmd = binPath(self.cmdFile)
        else:
            cmd = self.cmdFile
        parts = [cmd]
        endargs = ''
        props = getattr(context,'_properties')
        for p in props:
            ptype = p['type']
            switch = p['switch']
            value = getattr(context,p['id'])
            if value is not None and len(str(value)) > 0:
                if switch != 'None':
                    if ptype == 'boolean':
                        if value == True:
                            parts.append('%s' % switch)
                    elif ptype == 'list' or ptype == 'lines':
                        bySpace = value.split(' ')
                        byNewline = value.split('\n')
                        if len(bySpace) > len(byNewline):
                            endargs = '%s \"%s\"' % (switch, ' '.join(bySpace))
                        else:
                            endargs = '%s \"%s\"' % (switch, ' '.join(byNewline))
                    else:
                        if len(str(value)) > 0:
                            parts.append('%s \"%s\" ' % (switch, str(value)))
        parts.append(endargs)
        cmd = ' '.join(parts)
        cmd = RRDDataSource.getCommand(self, context, cmd)
        return cmd


    def checkCommandPrefix(self, context, cmd):
    	if self.provided == True:
            return self.getZenPack(context).path('libexec', cmd)
        else:
            return cmd
            
    def addDataPoints(self):
        for p in self.dpoints:
            if not self.datapoints._getOb(p, None):
                self.manage_addRRDDataPoint(p)
    
    def zmanage_editProperties(self, REQUEST=None):
        '''validation, etc'''
        if REQUEST:
            # ensure default datapoint didn't go away
            self.addDataPoints()
            # and eventClass
            if not REQUEST.form.get('eventClass', None):
                REQUEST.form['eventClass'] = self.__class__.eventClass
        return RRDDataSource.zmanage_editProperties(self, REQUEST)

