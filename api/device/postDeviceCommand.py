# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import ApiRequest
from api.common.api import RequestBody
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage
from api.device import status


# 下发指令
class PostDeviceCommandReq(ApiRequest, RequestBody):
    def __init__(self, devId, commands):
        self.setMethod(Constants.RequestPost)
        api = str.format(Constants.API_GET_DEVICE_STATUS, devId)
        self.setApi(api)
        if isinstance(commands, list):
            for c in commands:
                if not isinstance(c, dict):
                    raise Exception()
