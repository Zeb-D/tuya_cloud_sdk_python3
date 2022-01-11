# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage
from api.device import status


# 获取设备状态
class GetDeviceStatusReq(ApiRequest):
    def __init__(self, devId):
        self.setMethod(Constants.RequestGet)
        api = str.format(Constants.API_GET_DEVICE_STATUS, devId)
        self.setApi(api)


def GetDeviceStatus(devId):
    req = GetDeviceStatusReq(devId)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    result = resp['result']
    if isinstance(result, list):
        return status.object_hook_status(result)
