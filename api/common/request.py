# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
import hashlib
import json
import time
import logging
import requests
import urllib3
from api.common.constants import Constants
from api.common.api import RequestBody
from api.common import getToken
from config.config import EnvConfig


def DoRequest(ApiRequest, TokenManage):
    path = ApiRequest.getApi()
    method = ApiRequest.getMethod()
    timestamp = int(round(time.time() * 1000))
    token = TokenManage.getToken()
    access_token = None
    if isinstance(token, getToken.TokenResponse):
        access_token = token.accessToken
    if access_token is None:
        raise Exception(Constants.ERROR_TOKEN_NONE)

    sign_type = "HMAC-SHA256"
    sign = calc256Sign(clientId=EnvConfig.getAccessID(),
                       access_token=access_token,
                       secret=EnvConfig.getAccessKey(),
                       timestamp=str(timestamp))

    hs = {
        "Content-Type": "application/json;charset=UTF-8",
        "client_id": EnvConfig.getAccessID(),
        "sign": sign,
        "access_token": access_token,
        "t": str(timestamp),
        "sign_method": sign_type,
    }

    body = None
    if isinstance(ApiRequest, RequestBody):
        body = ApiRequest.getBody()

    resp = Do_RequestWeb(path, toBodyStr(body), method, hs)
    resp = toResultJson(resp)

    return resp


def Do_RequestWeb(path, body, method="GET", headers=None, islog=True, timeout=60):
    url = '%s%s' % (EnvConfig.getServerHost(), path)
    hs = headers if headers else {}

    hs['Connection'] = 'close'
    try:
        urllib3.disable_warnings()
        resp = requests.request(method, url, data=body, headers=hs, verify=False, timeout=timeout).text
        if islog:
            logging.info(
                "request[url:%s, method:%s, headers:%s, body:%s] resp:%s" % (url, method, headers, body, resp))
        return resp
    except BaseException as e:
        raise Exception("request failed", e.args)


def calc256Sign(clientId, secret, access_token, timestamp):
    s1 = clientId + access_token + timestamp
    import hmac
    h2 = hmac.new(secret.encode('utf-8'), s1.encode('utf-8'), digestmod=hashlib.sha256)
    s = h2.hexdigest()
    s = s.upper()
    return s


def calcSign(clientId, access_token, secret, timestamp):
    s = clientId + access_token + secret + timestamp
    m2 = hashlib.md5()
    m2.update(s.encode('utf-8'))
    sign = m2.hexdigest()
    signUp = sign.upper()
    return signUp


def toBodyStr(b):
    if b is None:
        return
    if isinstance(b, dict) or isinstance(b, list):
        return json.dumps(b)
    return b


def toResultJson(b):
    return json.loads(b)
