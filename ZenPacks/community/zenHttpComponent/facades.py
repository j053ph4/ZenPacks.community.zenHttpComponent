import os,re
import logging
log = logging.getLogger('zen.zenHttpComponentfacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from HttpComponent import HttpComponent
from .interfaces import IzenHttpComponentFacade


class zenHttpComponentFacade(ZuulFacade):
    implements(IzenHttpComponentFacade)

    def addHttpComponent(self, ob, httpPort='80', httpUseSSL=False, httpUrl='/', httpAuthUser='', httpAuthPassword='', httpJsonPost='', httpFindString=''):
        """ Adds HTTP Component URL monitor"""
        id = ob.id + '_' + re.sub('[^A-Za-z0-9]+', '', httpUrl) + '_'+httpPort
        httpcomponent = HttpComponent(id)
        ob.httpComponents._setObject(httpcomponent.id, httpcomponent)
        httpcomponent = ob.httpComponents._getOb(httpcomponent.id)
        httpcomponent.httpIp = ob.manageIp
        httpcomponent.httpPort = httpPort
        httpcomponent.httpUseSSL = httpUseSSL
        httpcomponent.httpUrl = httpUrl
        httpcomponent.httpAuthUser = httpAuthUser
        httpcomponent.httpAuthPassword = httpAuthPassword
        httpcomponent.httpJsonPost = httpJsonPost
        httpcomponent.httpFindString = httpFindString

        return True, _t(" Added URL Monitor for device %s" % (ob.id))
