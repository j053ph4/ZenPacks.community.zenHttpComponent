from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces import IFacade

class IHttpComponentInfo(IComponentInfo):
    """
    Info adapter for HttpComponent components.
    """
    httpIp = schema.Text(title=u"IP")
    httpPort = schema.Text(title=u"Port")
    httpUrl = schema.Text(title=u"Url")
    httpEventComponent = schema.Text(title=u"EventComponent")
    httpEventKey = schema.Text(title=u"Event Key")
    httpJsonPost = schema.Text(title=u"JSON String")
    httpFindString = schema.Text(title=u"Find String")
    httpAuthUser = schema.Text(title=u"User")
    httpAuthPassword = schema.Password(title=u"Password")
    httpUseSSL = schema.Bool(title=u"SSL")
    
class IzenHttpComponentFacade(IFacade):
    
    def addHttpComponent(self, ob, httpPort, httpUseSSL, httpUrl, httpAuthUser, httpAuthPassword, httpJsonPost, httpFindString):
        """  add HTTP Component to device
        """
