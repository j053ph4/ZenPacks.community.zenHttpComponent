'''
args:  compFacade,compClass,facadeName,iFacadeName,facadeMethodName, createMethod, singular
'''

import os,re
import logging
log = logging.getLogger('zen.zenHttpComponentFacade')

from zope.interface import implements
from Products.Zuul.facades import ZuulFacade
from Products.Zuul.utils import ZuulMessageFactory as _t
from HttpComponent import *
from .interfaces import *

class zenHttpComponentFacade(ZuulFacade):
    implements(IzenHttpComponentFacade)
    
    def addHttpComponent(self, ob, **kwargs):
    	target = ob
    
        from Products.ZenUtils.Utils import prepId
        from ZenPacks.community.zenHttpComponent.HttpComponent import HttpComponent
        import re
        cid = 'httpcomponent' 
        for k,v in kwargs.iteritems():
            if type(v) != bool:
                cid += str(v)
        cid = re.sub('[^A-Za-z0-9]+', '_', cid)
        id = prepId(cid)
        component = HttpComponent(id)
        relation = target.os.httpComponents
        relation._setObject(component.id, component)
        component = relation._getOb(component.id)
        for k,v in kwargs.iteritems():
            setattr(component,k,v) 
        
        setattr(component,"ip",target.manageIp)
        setattr(component,"hostname",target.id)
    
    
    

    	return True, _t("Added Monitored URL for device " + target.id)

