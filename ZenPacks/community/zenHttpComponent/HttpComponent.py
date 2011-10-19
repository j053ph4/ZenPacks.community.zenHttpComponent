################################################################################
#
# This program is part of the zenHttpComponent Zenpack for Zenoss.
# Copyright (C) 2011 ATX Group, Inc.
#
# This program can be used under the GNU General Public License version 2
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

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

    _properties = (
        {'id':'httpUrl', 'type':'string', 'mode':''},
        {'id':'httpPort', 'type':'string', 'mode':''},
        {'id':'httpAuthUser', 'type':'string', 'mode':''},
        {'id':'httpAuthPassword', 'type':'string', 'mode':''},
        {'id':'httpFindString', 'type':'string', 'mode':''},
        {'id':'httpJsonPost', 'type':'string', 'mode':''},
        )

    _relations = (
        ('httpDevice', ToOne(ToManyCont,'ZenPacks.community.zenHttpComponent.HttpDevice', 'httpComponent')),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
        },),
    },)
    
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
    
    def monitored(self):
        return True
