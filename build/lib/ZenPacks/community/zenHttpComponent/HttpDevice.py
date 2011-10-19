######################################################################
#
# HttpDevice object class
#
######################################################################
from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenWidgets import messaging

class HttpDevice(Device):
    """
    HttpDevice is the base class to contain components describing HTTP URL checks
    """
    
    meta_type = portal_type = 'HttpDevice'

    _relations = Device._relations + (
        ('httpComponents', ToManyCont(ToOne,
            'ZenPacks.community.zenHttpComponent.HttpComponent', 'httpDevice')),
        )

    def createHttpComponent(self, id, httpPort=80, httpURL='/',httpAuthUser=None, httpAuthPassword=None,\
                                httpEventComponent='URL',httpEventKey='HTTP',httpJsonPost=None,httpFindString=None):
        """
        """
        from HttpComponent import HttpComponent
        httpcomponent = HttpComponent(id)
        self.httpComponents._setObject(httpcomponent.id, rule)
        httpcomponent = self.httpComponents._getOb(httpcomponent.id)
        httpcomponent.httpPort = httpPort
        httpcomponent.httpURL = self.httpURL
        httpcomponent.httpAuthUser = self.httpAuthUser
        httpcomponent.httpAuthPassword = httpAuthPassword
        httpcomponent.httpEventComponent = httpEventComponent
        httpcomponent.httpEventKey = httpEventKey
        httpcomponent.httpJsonPost = httpJsonPost
        httpcomponent.httpFindString = httpFindString
        return httpcomponent
    
    def manage_addHttpComponent(self, id, httpPort=80, httpURL='/',httpAuthUser=None, httpAuthPassword=None,\
                                httpEventComponent='URL',httpEventKey='HTTP',httpJsonPost=None,httpFindString=None):
        """
        """
        self.createHttpComponent(id, httpPort, httpURL, httpAuthUser, httpAuthPassword, httpEventComponent, httpEventKey, httpJsonPost, httpFindString)
        if REQUEST:
            messaging.IMessageSender(self).sendToBrowser(
                'HTTP URL Monitor Created',
                'HTTP URL Monitor %s was created.' % httpURL
            )
            return self.callZenScreen(REQUEST)

