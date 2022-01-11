# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm

import time
from config.config import EnvConfig
from api.common import request


def DoRequestForToken(ApiRequest):
    path = ApiRequest.getApi()
    method = ApiRequest.getMethod()
    timestamp = int(round(time.time() * 1000))

    sign_type = "HMAC-SHA256"
    sign = request.calc256Sign(clientId=EnvConfig.getAccessID(),
                               access_token='',
                               secret=EnvConfig.getAccessKey(),
                               timestamp=str(timestamp))

    hs = {
        "Content-Type": "application/json;charset=UTF-8",
        "client_id": EnvConfig.getAccessID(),
        "sign": sign,
        "t": str(timestamp),
        "sign_method": sign_type,
    }

    resp = request.Do_RequestWeb(path, None, method, hs)
    resp = request.toResultJson(resp)

    return resp
