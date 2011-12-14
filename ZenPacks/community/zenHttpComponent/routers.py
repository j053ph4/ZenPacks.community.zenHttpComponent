from Products.ZenUtils.Ext import DirectRouter, DirectResponse
from Products import Zuul


class zenHttpComponentRouter(DirectRouter):
    def _getFacade(self):
        return Zuul.getFacade('zenHttpComponentAdapter', self.context)

    def addHttpComponentRouter(self, httpPort, httpUseSSL, httpUrl, httpAuthUser, httpAuthPassword, httpJsonPost, httpFindString):
        
        facade = self._getFacade()

        ob = self.context
        success, message = facade.addHttpComponent(ob, httpPort, httpUseSSL, httpUrl, httpAuthUser, httpAuthPassword, httpJsonPost, httpFindString)
        if success:
            return DirectResponse.succeed(message)
        else:
            return DirectResponse.fail(message) 
