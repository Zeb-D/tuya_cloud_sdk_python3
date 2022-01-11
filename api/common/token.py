# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.common.api import TokenManage
from api.common.getToken import GetSimpleToken


class LocalTokenManage(TokenManage):
    def getToken(self):
        return GetSimpleToken()


# 实现者，需要重新赋值
LocalTokenManage = LocalTokenManage()
