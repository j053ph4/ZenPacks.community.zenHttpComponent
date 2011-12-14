import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
import os,re

unused(Globals)
""" Add device relations
"""
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
Device._relations += (('httpComponents', ToManyCont(ToOne,'ZenPacks.community.zenHttpComponent.HttpComponent','httpDevice')),)

from Products.ZenUtils.Utils import monkeypatch,prepId

@monkeypatch('Products.ZenModel.Device.Device')
def manage_addHttpComponent(self, httpPort='80', httpUseSSL=False, httpUrl='/', httpAuthUser='', httpAuthPassword='', httpJsonPost='', httpFindString=''):
    """make a http component"""
    from HttpComponent import HttpComponent
    
    newId = self.id + '_' + re.sub('[^A-Za-z0-9]+', '', httpUrl) + '_'+httpPort
    hcid = prepId(newId)
    httpcomponent = HttpComponent(hcid)
    self.httpComponents._setObject(httpcomponent.id, httpcomponent)
    httpcomponent = self.httpComponents._getOb(httpcomponent.id)
    httpcomponent.httpIp = self.manageIp
    httpcomponent.httpPort = httpPort
    httpcomponent.httpUrl = httpUrl
    httpcomponent.httpUseSSL = httpUseSSL
    httpcomponent.httpAuthUser = httpAuthUser
    httpcomponent.httpAuthPassword = httpAuthPassword
    httpcomponent.httpJsonPost = httpJsonPost
    httpcomponent.httpFindString = httpFindString
    return httpcomponent

class ZenPack(ZenPackBase):
    """ HTTP Component
    """

    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()

    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        Device._relations = tuple([x for x in Device._relations if x[0] not in ('httpComponents')])
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()
