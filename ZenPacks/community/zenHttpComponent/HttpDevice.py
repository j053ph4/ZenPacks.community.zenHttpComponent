######################################################################
#
# HttpDevice object class
#
######################################################################
from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenWidgets import messaging
from copy import deepcopy
from AccessControl import Permissions

class HttpDevice(Device):
    """
    HttpDevice is the base class to contain components describing HTTP URL checks
    """
    
    meta_type = portal_type = 'HttpDevice'

    _relations = Device._relations + (
        ('httpComponents', ToManyCont(ToOne,
            'ZenPacks.community.zenHttpComponent.HttpComponent', 'httpDevice')),
        )

    factory_type_information = deepcopy(Device.factory_type_information)
    factory_type_information[0]['actions'] += (
            { 'id'              : 'HttpDevice'
            , 'name'            : 'Manage URLs'
            , 'action'          : 'manageURLs'
            , 'permissions'     : ( Permissions.view,) },
            )

    def getURLs(self):
        return self.httpComponents()

    def deleteURLs(self, ids=[], REQUEST=None):
        """ Delete selected URLs
        """
        for url in self.httpComponents():
            id = getattr(url, 'id', None)
            if id in ids:
                self.httpComponents._delObject(id)
        if REQUEST:
            messaging.IMessageSender(self).sendToBrowser(
                'URLs Deleted',
                'URLs deleted: %s' % (', '.join(ids))
            )
            return self.callZenScreen(REQUEST)

    def createHttpComponent(self, id, httpPort=80, httpURL='/',httpAuthUser='', httpAuthPassword='',\
                            httpJsonPost='',httpFindString=''):
        """
        """
        from HttpComponent import HttpComponent
        httpcomponent = HttpComponent(id)
        self.httpComponents._setObject(httpcomponent.id, httpcomponent)
        httpcomponent = self.httpComponents._getOb(httpcomponent.id)
        httpcomponent.httpPort = httpPort
        httpcomponent.httpURL = httpURL
        httpcomponent.httpAuthUser = httpAuthUser
        httpcomponent.httpAuthPassword = httpAuthPassword
        httpcomponent.httpJsonPost = httpJsonPost
        httpcomponent.httpFindString = httpFindString
        return httpcomponent
    
    def manage_addHttpComponent(self, id, httpPort=80, httpURL='/',httpAuthUser='', httpAuthPassword='',\
                                httpJsonPost='',httpFindString='',REQUEST=''):
        """
        """
        self.createHttpComponent(id, httpPort, httpURL, httpAuthUser, httpAuthPassword, httpJsonPost, httpFindString)
        if REQUEST:
            messaging.IMessageSender(self).sendToBrowser(
                'HTTP URL Monitor Created',
                'HTTP URL Monitor %s was created.' % httpURL
            )
            return self.callZenScreen(REQUEST)

