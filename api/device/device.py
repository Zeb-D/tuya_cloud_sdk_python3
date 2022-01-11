# coding: utf-8
# Author：Zeb灬D
# Date ：2020-01-13 10:23
# Tool ：PyCharm
from api.device import status


class Device(object):
    def __init__(self):
        self.uid = None
        self.uuid = None
        self.time_zone = None
        self.sub = None
        self.status = None
        self.product_id = None
        self.owner_id = None
        self.online = None
        self.name = None
        self.local_key = None
        self.ip = None
        self.id = None
        self.icon = None
        self.category = None
        self.active_time = None


def object_hook_device(deviceStatus):
    if isinstance(deviceStatus, dict):
        dr = Device()
        dr.uid = deviceStatus.get('uid')
        dr.uuid = deviceStatus.get('uuid')
        dr.time_zone = deviceStatus.get('time_zone')
        dr.sub = deviceStatus.get('sub')
        dr.status = status.object_hook_status(deviceStatus.get('status'))
        dr.product_id = deviceStatus.get('product_id')
        dr.owner_id = deviceStatus.get('owner_id')
        dr.online = deviceStatus.get('online')
        dr.name = deviceStatus.get('name')
        dr.local_key = deviceStatus.get('local_key')
        dr.ip = deviceStatus.get('ip')
        dr.id = deviceStatus.get('id')
        dr.icon = deviceStatus.get('icon')
        dr.category = deviceStatus.get('category')
        dr.active_time = deviceStatus.get('active_time')
        return dr
