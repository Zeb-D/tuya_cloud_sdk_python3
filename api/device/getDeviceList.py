# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
import json
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.common.request import DoRequest
from api.common.token import LocalTokenManage
from api.device.status import DeviceStatus
from api.device import device


# 批量获取设备信息
class GetDeviceListReq(ApiRequest):
    # deviceIds 逗号相接："aaa,vvb"
    def __init__(self, deviceIds, pageNo, pageSize):
        self.setMethod(Constants.RequestGet)
        if pageNo is None:
            pageNo = 1
        if pageSize is None:
            pageSize = 50
        if deviceIds is None:
            raise Exception(Constants.ERROR_PARAM_NONE)
        api = str.format(Constants.API_GET_DEVICE_LIST, deviceIds, pageNo, pageSize)
        self.setApi(api)


class GetDeviceListResponse(object):
    def __init__(self):
        self.total = 0,
        self.devices = []


def ToGetDeviceListResponse(result):
    if isinstance(result, dict):
        rsp = GetDeviceListResponse()
        rsp.total = result.get("total")
        devices = result.get("devices")
        if isinstance(devices, list):
            varList = []
            for deviceStatus in devices:
                d = device.object_hook_device(deviceStatus)
                varList.append(d)
            rsp.devices = varList
        return rsp


def GetDeviceList(deviceIds, pageNo, pageSize):
    req = GetDeviceListReq(deviceIds, pageNo, pageSize)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    return ToGetDeviceListResponse(resp['result'])
