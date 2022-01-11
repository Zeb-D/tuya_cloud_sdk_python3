# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import ApiRequest
from api.common.constants import Constants
from api.device import function
from api.common.request import DoRequest
from api.common.token import LocalTokenManage


# 获取某个设备指令集
class GetDeviceFunctionsReq(ApiRequest):
    def __init__(self, deviceId):
        self.setMethod(Constants.RequestGet)
        api = str.format(Constants.API_GET_DEVICE_FUNCTIONS, deviceId)
        self.setApi(api)


class DeviceFunction(object):
    def __init__(self):
        self.category = None
        self.functions = None


def ToDeviceFunction(deviceFunction):
    if isinstance(deviceFunction, dict):
        df = DeviceFunction()
        df.category = deviceFunction.get("category")
        functions = deviceFunction.get("functions")
        if isinstance(functions, list):
            varList = []
            for f in functions:
                if isinstance(f, dict):
                    varList.append(function.ToFunction(f))
            df.functions = varList
        return df


# 获取设备指令
def GetDeviceFunction(devId):
    req = GetDeviceFunctionsReq(devId)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    return ToDeviceFunction(resp['result'])


# 获取类型下的指令集
class GetDeviceFunctionByCategoryReq(ApiRequest):
    def __init__(self, category):
        self.setMethod(Constants.RequestGet)
        api = str.format(Constants.API_GET_DEVICE_FUNCTIONS_BY, category)
        self.setApi(api)


def GetDeviceFunctionByCategory(category):
    req = GetDeviceFunctionByCategoryReq(category)
    resp = DoRequest(req, LocalTokenManage)
    if not resp['success']:
        raise Exception(resp)
    return ToDeviceFunction(resp['result'])
