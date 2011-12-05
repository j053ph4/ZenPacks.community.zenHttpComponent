from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from ZenPacks.community.zenHttpComponent.interfaces import IHttpComponentInfo

class HttpComponentInfo(ComponentInfo):
    """
    Info adapter for HttpComponent components.
    """
    implements(IHttpComponentInfo)
    httpPort = ProxyProperty("httpPort")
    httpUrl = ProxyProperty("httpUrl")
    httpEventComponent = ProxyProperty("httpEventComponent")
    httpEventKey = ProxyProperty("httpEventKey")
    httpJsonPost = ProxyProperty("httpJsonPost")
    httpFindString = ProxyProperty("httpFindString")
    httpAuthUser = ProxyProperty("httpAuthUser")
    httpAuthPassword = ProxyProperty("httpAuthPassword")
