# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm

class _const:

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.Exception("can't change const %s" % name)
        self.__dict__[name] = value


Constants = _const()

Constants.URLCN = "https://openapi.tuyacn.com"
Constants.URLCNPre = "https://openapi-cn.wgine.com"

Constants.URLUS = "https://openapi.tuyaus.com"

Constants.URLEU = "https://openapi.tuyaeu.com"

Constants.URLIN = "https://openapi.tuyain.com"

Constants.RequestGet = "GET"
Constants.RequestPost = "POST"
Constants.RequestPut = "PUT"
Constants.RequestDelete = "DELETE"

Constants.ERROR_METHOD_NONE = "method is none"
Constants.ERROR_API_NONE = "api is none"
Constants.ERROR_BODY_NONE = "request body is none"
Constants.ERROR_TOKEN_NONE = "TokenManage's token is None"
Constants.ERROR_PARAM_NONE = "param is empty"

# token 相关
Constants.API_GET_TOKEN = "/v1.0/token?grant_type=1"
Constants.API_GET_REFESHTOKEN = "/v1.0/token/{}"

# 设备相关
Constants.API_DELETE_DEVICE = "/v1.0/devices/{}"
Constants.API_GET_DEVICE = "/v1.0/devices/{}"
Constants.API_GET_DEVICE_LIST = "/v1.0/devices?device_ids={}&page_no={}&page_size={}"
Constants.API_GET_DEVICE_FUNCTIONS = "/v1.0/devices/{}/functions"
Constants.API_GET_DEVICE_FUNCTIONS_BY = "/v1.0/functions/{}"
Constants.API_GET_DEVICE_STATUS = "/v1.0/devices/{}/status"

# 用户相关
Constants.API_GET_USER_DEVICE_LIST = "/v1.0/user/devices"