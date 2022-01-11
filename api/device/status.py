# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
class DeviceStatus(object):
    def __init__(self):
        self.code = None
        self.value = None


def object_hook_status(status):
    if isinstance(status, dict):
        ds = DeviceStatus()
        ds.code = status.get('code')
        ds.value = status.get('value')
        return ds
    if isinstance(status, list):
        varList = []
        for s in status:
            if isinstance(s, dict):
                ds = DeviceStatus()
                ds.code = s.get('code')
                ds.value = s.get('value')
                varList.append(ds)
        return varList