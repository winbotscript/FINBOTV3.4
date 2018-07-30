from ..finbot.ttypes import Message
from .finbotClient import FinbotApi
from .finbots import FinBots
from .bot import Bots
from .call import Call
from .timeline import Timeline

class FINBOTV1(FinbotApi, FinBots, Bots, Call, Timeline):

    def __init__(self, idOrAuthToken=None, passwd=None, certificate=None, systemName=None, appName=None, showQr=False, keepLoggedIn=True):
        
        FinbotApi.__init__(self)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if idOrAuthToken and passwd:
            self.loginWithCredential(_id=idOrAuthToken, passwd=passwd, certificate=certificate, systemName=systemName, appName=appName, keepLoggedIn=keepLoggedIn)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(authToken=idOrAuthToken, appName=appName)

        self.__initAll()

    def __initAll(self):
        self.profile    = self.talk.getProfile()
        self.groups     = self.talk.getGroupIdsJoined()
        FinBots.__init__(self)
        Bots.__init__(self)
        Call.__init__(self)
        Timeline.__init__(self)