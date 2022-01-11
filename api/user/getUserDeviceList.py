# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
import json
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage
from api.device import device


# 批量获取设备信息
class GetUserDeviceListReq(ApiRequest):
    def __init__(self):
        self.setMethod(Constants.RequestGet)
        self.setApi(Constants.API_GET_USER_DEVICE_LIST)


def GetUserDeviceList():
    req = GetUserDeviceListReq()
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    result = resp['result']
    varlist = []
    if isinstance(result, list):
        for dev in result:
            ds = device.object_hook_device(dev)
            varlist.append(ds)
    return varlist
