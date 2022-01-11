# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage


# 删除某个设备
class DeleteDeviceReq(ApiRequest):
    def __init__(self, deviceId):
        self.setMethod(Constants.RequestDelete)
        api = str.format(Constants.API_DELETE_DEVICE, deviceId)
        self.setApi(api)


def DeleteDevice(deviceId):
    req = DeleteDeviceReq(deviceId)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    return resp['result']
