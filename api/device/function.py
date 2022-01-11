# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm

class Function(object):
    def __init__(self):
        self.name = None
        self.desc = None
        self.code = None
        self.type = None
        self.values = None

def ToFunction(function):
    if isinstance(function,dict):
       f = Function()
       f.name = function.get("name")
       f.desc = function.get("desc")
       f.code = function.get("code")
       f.type = function.get("type")
       f.values = function.get("values")
       return f