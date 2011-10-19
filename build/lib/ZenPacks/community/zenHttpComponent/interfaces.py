from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

class IHttpComponentInfo(IComponentInfo):
    """
    Info adapter for HttpComponent components.
    """
    httpPort = schema.Text(title=u"Port")
    httpUrl = schema.Text(title=u"Url")
    httpEventComponent = schema.Text(title=u"EventComponent")
    httpEventKey = schema.Text(title=u"Event Key")
    httpJsonPost = schema.Text(title=u"JSON String")
    httpFindString = schema.Text(title=u"Find String")

