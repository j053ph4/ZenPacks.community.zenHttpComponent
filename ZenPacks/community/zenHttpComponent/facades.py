import os
import logging
log = logging.getLogger('zen.zenHttpComponentfacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from HttpComponent import HttpComponent
from .interfaces import IzenHttpComponentFacade


class zenHttpComponentFacade(ZuulFacade):
    implements(IzenHttpComponentFacade)

    def addHttpComponent(self, ob, httpPort='80', httpUrl='/', httpAuthUser='', httpAuthPassword='', httpJsonPost='', httpFindString=''):
        """ Adds HTTP Component URL monitor"""
        id = ob.id + '_' + httpUrl.replace('/','_') + '_'+httpPort
        httpcomponent = HttpComponent(id)
        ob.httpComponents._setObject(httpcomponent.id, httpcomponent)
        httpcomponent = ob.httpComponents._getOb(httpcomponent.id)
        httpcomponent.httpPort = httpPort
        httpcomponent.httpUrl = httpUrl
        httpcomponent.httpAuthUser = httpAuthUser
        httpcomponent.httpAuthPassword = httpAuthPassword
        httpcomponent.httpJsonPost = httpJsonPost
        httpcomponent.httpFindString = httpFindString

        return True, _t(" Added URL Monitor for device %s" % (ob.id))
