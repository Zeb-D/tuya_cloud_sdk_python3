# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage
from api.device import device


# 获取某个设备详情
class GetDeviceReq(ApiRequest):
    def __init__(self, deviceId):
        self.setMethod(Constants.RequestGet)
        api = str.format(Constants.API_GET_DEVICE, deviceId)
        self.setApi(api)


def GetDeviceById(deviceId):
    req = GetDeviceReq(deviceId)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    return device.object_hook_device(resp['result'])
