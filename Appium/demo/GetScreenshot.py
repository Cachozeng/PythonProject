import os
import time
from appium import webdriver

desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'TAG-TL00',
                'noReset': True,
                'appPackage': 'com.baidu.searchbox',
                'appActivity': 'com.baidu.searchbox.SplashActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app
time.sleep(3)  # app启动后等待3秒，方便元素加载完成

# 截图
img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
time =time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_save_path = img_folder + time + '.png'
driver.get_screenshot_as_file(screen_save_path)

