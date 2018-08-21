from FinbotServer.transport import THttpClient
from FinbotServer.protocol import TCompactProtocol
from ..finbot import AuthService, TalkService, ChannelService, CallService

class Session:
    def __init__(self, url, headers, path=''):
        self.host = url + path
        self.headers = headers

    def Api(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.auth  = AuthService.Client(self.protocol)
        if isopen:
            self.transport.open()
        return self.auth

    def Bots(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.talk  = TalkService.Client(self.protocol)
        if isopen:
            self.transport.open()
        return self.talk

    def Channel(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.channel  = ChannelService.Client(self.protocol)
        if isopen:
            self.transport.open()
        return self.channel

    def Call(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.call  = CallService.Client(self.protocol)
        if isopen:
            self.transport.open()
        return self.call