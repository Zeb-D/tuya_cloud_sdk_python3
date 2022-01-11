# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
import time
import threading
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common import request_token


class TokenRequest(ApiRequest):
    def __init__(self):
        self.setApi(Constants.API_GET_TOKEN)
        self.setMethod(Constants.RequestGet)


class TokenResponse(object):
    def __init__(self):
        self.accessToken = None
        self.expireTime = None
        self.refreshToken = None
        self.uid = None
        self.expireAt = int(round(time.time() * 1000))

    def __str__(self):
        return '[accessToken:%s ,expireTime:%s ,refreshToken:%s ,uid:%s]' % \
               (self.accessToken, self.expireTime, self.refreshToken, self.uid)


Token_Request = TokenRequest()
Local_Token = TokenResponse()
TokenLock = threading.Lock()


def LocalTokenIsNone():
    if Local_Token is None:
        return None
    TokenLock.acquire()
    try:
        if Local_Token.accessToken is None:
            return None
        if Local_Token.refreshToken is None:
            return None
        # 判断有效期，小于300s
        if Local_Token.expireAt - int(round(time.time() * 1000)) < 300:
            # 刷新下token
            return GetRefreshToken(Local_Token.refreshToken)
        else:
            return Local_Token
    finally:
        TokenLock.release()


# 简单模式获取token
def GetSimpleToken():
    localT = LocalTokenIsNone()
    if not localT is None:
        return localT
    resp = request_token.DoRequestForToken(Token_Request)
    if not resp['success']:
        raise Exception(resp)
    tokenResponse = TokenResponse()
    tokenResponse.accessToken = resp['result']['access_token']
    tokenResponse.refreshToken = resp['result']['refresh_token']
    tokenResponse.expireTime = resp['result']['expire_time']
    tokenResponse.uid = resp['result']['uid']
    global Local_Token
    Local_Token = tokenResponse
    Local_Token.expireAt = int(round(time.time() * 1000)) + Local_Token.expireTime
    return tokenResponse


class RefreshTokenRequest(ApiRequest):
    def __init__(self, refreshToken):
        self.setMethod(Constants.RequestGet)
        api = str.format(Constants.API_GET_REFESHTOKEN, refreshToken)
        self.setApi(api)


def GetRefreshToken(refreshToken):
    req = RefreshTokenRequest(refreshToken)
    resp = request_token.DoRequestForToken(req)
    if not resp['success']:
        return None  # 这里没有刷新成功则，则将于GetToken一次
    tokenResponse = TokenResponse()
    tokenResponse.accessToken = resp['result']['access_token']
    tokenResponse.refreshToken = resp['result']['refresh_token']
    tokenResponse.expireTime = resp['result']['expire_time']
    tokenResponse.uid = resp['result']['uid']
    global Local_Token
    Local_Token = tokenResponse
    Local_Token.expireAt = int(round(time.time() * 1000)) + Local_Token.expireTime
    return tokenResponse
