import os

import time
from appium import webdriver

apk_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # 获取当前项目的根路径

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 设备系统
desired_caps['platformVersion'] = '5.1'  # 设备系统版本
desired_caps['deviceName'] = 'TAG-TL00'  # 设备名称

# 测试apk包的路径
desired_caps['app'] = apk_path + '\\app\\shoujibaidu.apk'
# 不需要每次都安装apk
desired_caps['noReset'] = True
# 应用程序的包名
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

time.sleep(5)  # app启动后等待5秒，方便元素加载完成

# 根据元素id来定位
# 点击“热点”频道
# hot = driver.find_element_by_id('com.baidu.searchbox:id/tab_indi_title')
hot = driver.find_element_by_android_uiautomator("text(\"热点\")")
hot.click()
# 点击“推荐”频道
rec = driver.find_element_by_android_uiautomator("text(\"推荐\")")
rec.click()
driver.quit()