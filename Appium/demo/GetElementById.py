import os

import time
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '5.1'  # 设备系统版本
desired_caps['deviceName'] = 'TAG-TL00'  # 设备名称

# 测试apk包的路径
#desired_caps['app'] = apk_path + '\\app\\kuaibao.apk'

# 不需要每次都安装apk
desired_caps['noReset'] = True

# 应用程序的包名
desired_caps['appPackage'] = 'com.tencent.reading'
desired_caps['appActivity'] = 'com.tencent.reading.activity.SplashActivity'
# 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(5)  # app启动后等待5秒，方便元素加载完成
# 根据元素id来定位
driver.find_element_by_id('com.tencent.reading:id/list_title_text').click()