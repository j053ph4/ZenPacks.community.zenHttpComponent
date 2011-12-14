################################################################################
#
# This program is part of the zenHttpComponent Zenpack for Zenoss.
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Globals import DTMLFile

#def manage_addHttpComponent(context, httpPort='80', httpUrl='/', httpAuthUser='', httpAuthPassword='', httpJsonPost='', httpFindString='', REQUEST=None):
#    """make a http component"""
#    id = httpUrl.replace('/','_') + '_'+httpPort
#    hcid = prepId(newId)
#    httpcomponent = HttpComponent(id)
#    
#    context._setObject(httpcomponent.id, httpcomponent)
#    httpcomponent = context._getOb(httpcomponent.id)
#    httpcomponent.httpPort = httpPort
#    httpcomponent.httpUrl = httpUrl
#    httpcomponent.httpAuthUser = httpAuthUser
#    httpcomponent.httpAuthPassword = httpAuthPassword
#    httpcomponent.httpJsonPost = httpJsonPost
#    httpcomponent.httpFindString = httpFindString
#    if REQUEST is not None:
#        REQUEST['RESPONSE'].redirect(context.absolute_url()+'/manage_main')
#        
class HttpComponent(DeviceComponent, ManagedEntity):
    """
    HttpComponent contains the basic properties of a HttpComponent
    """
    portal_type = meta_type = 'HttpComponent'

    httpUrl = '/'
    httpPort = '80'
    httpAuthUser = None
    httpAuthPassword = None
    httpJsonPost = None
    httpFindString = None
    httpEventComponent = 'URL'
    httpEventKey = 'WWW'
    
    _properties = (
        {'id':'httpUrl', 'type':'string', 'mode':''},
        {'id':'httpPort', 'type':'string', 'mode':''},
        {'id':'httpAuthUser', 'type':'string', 'mode':''},
        {'id':'httpAuthPassword', 'type':'string', 'mode':''},
        {'id':'httpFindString', 'type':'string', 'mode':''},
        {'id':'httpJsonPost', 'type':'string', 'mode':''},
        {'id':'httpEventComponent', 'type':'string', 'mode':''},
        {'id':'httpEventKey', 'type':'string', 'mode':''},
        )

    _relations = (
        ('httpDevice', ToOne(ToManyCont,'Products.ZenModel.Device.Device', 'httpComponent')),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)
    
    isUserCreatedFlag = True
    def isUserCreated(self):
        return self.isUserCreatedFlag
    
    def viewName(self):
        return self.httpUrl
    titleOrId = name = viewName

    def primarySortKey(self):
        return self.httpUrl
    
    def getStatus(self):
        return self.statusMap()
    
    def statusMap(self):
        """ map run state to zenoss status
        """
        self.status = 0
        return self.status
    
    def device(self):
        return self.httpDevice()

    def manage_deleteComponent(self, REQUEST=None):
        url = None
        if REQUEST is not None:
            url = self.device().httpComponents.absolute_url()
        self.getPrimaryParent()._delObject(self.id)
        if REQUEST is not None:
            REQUEST['RESPONSE'].redirect(url)


