# -*- coding: utf-8 -*-

from config import config
from api.common.constants import Constants
from api.common import getToken
from api.device.getDeviceList import GetDeviceList
from api.user import getUserDeviceList

config.InitEnv(Constants.URLCN, "Your clientId/accessId", "Your secret")

if __name__ == "__main__":
    print(getToken.GetSimpleToken())
    print(getToken.Local_Token.accessToken)
    # print(getToken.GetSimpleToken())
    # print(getToken.GetRefreshToken(getToken.Local_Token.refreshToken))
    # print(GetDeviceList())
    r = getUserDeviceList.GetUserDeviceList()
    print(r[0].status[0].code)