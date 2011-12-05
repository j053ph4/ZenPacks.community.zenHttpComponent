import Globals
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase
from Products.ZenUtils.Utils import unused
import os

unused(Globals)
""" Add device relations
"""
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Device import Device
Device._relations += (('httpComponents', ToManyCont(ToOne,'ZenPacks.community.zenHttpComponent.HttpComponent','httpDevice')),)

class ZenPack(ZenPackBase):
    """ HTTP Component
    """

    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()
            
    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        
    def remove(self, app, leaveObjects=False):
        ZenPackBase.remove(self, app, leaveObjects)
        Device._relations = tuple([x for x in Device._relations if x[0] not in ('httpComponents')])
        for d in self.dmd.Devices.getSubDevices():
            d.buildRelations()
