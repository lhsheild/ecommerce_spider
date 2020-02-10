import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


inspector_capability_params = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True
}

if __name__ == '__main__':
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=inspector_capability_params)
    try:
        if WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath(
                "//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")):
            driver.find_element_by_xpath(
                "//android.view.View[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
            size = get_size()
            x1 = int(size[0] * 0.5)
            y1 = int(size[1] * 0.75)
            y2 = int(size[1] * 0.25)
            while True:
                driver.swipe(x1, y1, x1, y2)
                time.sleep(1)
    except Exception as e:
        print('没有该按钮---{}'.format(e))
        pass
