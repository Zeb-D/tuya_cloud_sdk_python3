# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.constants import Constants


# 相当于api接口请求，子类要setMethod、setApi
class ApiRequest(object):
    def __init__(self):
        self._method_ = None,
        self._api_ = None

    def setMethod(self, method):
        self._method_ = method

    def getMethod(self):
        if self._method_ is None:
            raise Exception(Constants.ERROR_METHOD_NONE)
        return self._method_

    def setApi(self, api):
        self._api_ = api

    def getApi(self):
        if self._api_ is None:
            raise Exception(Constants.ERROR_API_NONE)
        return self._api_


# 请求body体，需要重写setBody
class RequestBody(object):
    def __init__(self):
        self._body_ = None

    def setBody(self, body):
        self._body_ = body

    def getBody(self):
        return self._body_


# token管理器，需要实现着去实现
class TokenManage(object):
    def getToken(self):
        raise Exception(Constants.ERROR_TOKEN_NONE)
