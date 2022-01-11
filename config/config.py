# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm

class Config(object):

    def __init__(self):
        self.serverHost = ""
        self.accessID = ""
        self.accessKey = ""

    def setServerHost(self, serverHost):
        self.serverHost = serverHost

    def setAccessID(self, accessID):
        self.accessID = accessID

    def setAccessKey(self, accessKey):
        self.accessKey = accessKey

    def getServerHost(self):
        return self.serverHost

    def getAccessID(self):
        return self.accessID

    def getAccessKey(self):
        return self.accessKey

    def __str__(self):
        return '[serverHost:%s ,accessID:%s ,accessKey:%s]' % (self.serverHost, self.accessID, self.accessKey)


EnvConfig = Config()  # 全局配置


def InitEnv(host, clientId, secret):
    EnvConfig.setServerHost(host)
    EnvConfig.setAccessID(clientId)
    EnvConfig.setAccessKey(secret)
