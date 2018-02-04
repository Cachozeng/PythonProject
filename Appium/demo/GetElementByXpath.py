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

# 根据元素xpath来定位
# 点击“我的”
my_home = driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()

# 利用ui automator viewer给出的index的值来定位，发现有些定位不准
driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout' and @index='4']").click()
time.sleep(2)
driver.quit()