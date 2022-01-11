# tuya_cloud_sdk_python3
tuya developer could api python3 sdk

### Introduction

Tuya Cloud API SDK for python3.

### Get Started

Make sure you have serverHOST, AccessID and AccessKey.

Before running this SDK, you need to initialize it with the following method:

```
config.InitEnv(Constants.URLCN, "Your clientId/accessId", "Your secret")
```

### Example

If you want to fetch the device info, you can call device.GetDevice():

```
if __name__ == "__main__":
    print(getToken.GetSimpleToken())
    print(getToken.Local_Token.accessToken)
    # print(getToken.GetSimpleToken())
    # print(getToken.GetRefreshToken(getToken.Local_Token.refreshToken))
    # print(GetDeviceList())
    r = getUserDeviceList.GetUserDeviceList()
    print(r[0].status[0].code)
```

```
see also the code of Test.py, at the examples pls
```



### Support

You can get support from Tuya with the following methods:

- Tuya Smart Help Center: https://support.tuya.com/en/help
- Technical Support: https://iot.tuya.com/council
