from appium import webdriver

# 1、准备参数：哪个设备中的哪个app
# appium_connect = {
#     'appium:deviceName': '192.168.1.6:5555',
#     'appium:appPackage': "com.huawei.calculator",
#     'appium:appActivity': "com.huawei.calculator.Calculator",
#     'platformName': 'Android'
#     }
desired_caps = {
    "platformVersion": "12",
    "deviceName": "CET-AL60",
    "appPackage": "tv.danmaku.bili",
    "appActivity": ".MainActivityV2",
    "platformName": "Android",
    "noReset": True
}
# 2、连接appium server，发送启动参数
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)