import time
import os
from appium import webdriver
import random
from PIL import Image

desired_cap = {
        "platformName": "Android",
        "platformVersion": "11.0",
        "deviceName": "emulator-5554",
        "app": "C:\\Users\\agupta\\Downloads\\game-tv_1.0.28.apk"
    }
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)
def test_LaunchAndVerify():
    assert driver.find_element_by_xpath("//android.view.View[@content-desc = 'Enter your phone number']").is_displayed()

def test_TwitterIcon():
    assert driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='AuthoriseWithTwitter_593']").is_displayed()
    driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='AuthoriseWithTwitter_593']").click()
    time.sleep(5)
    cwd = os.getcwd()
    filename = str(random.random()).replace(".", "") + ".png"
    driver.save_screenshot(cwd + "\\" + filename)
    assert imageCompare("ReferenceFile.png", filename, 70)

def test_login():
    driver.back()
    driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.ImageView/android.view.View/android.widget.ImageView[2]").click()
    driver.find_element_by_id("(/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView)[1]").send_keys("tes1.auto1@gmail.com")
    driver.find_element_by_xpath("(/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView)[2]").send_keys("game@twitter")
    driver.find_element_by_id().click("next")
    assert driver.find_element_by_xpath("//android.view.View[@title = 'Game.tv']").is_displayed()







def imageCompare(ReferenceFile, ActualFile, tolerance):
    i1 = Image.open(ReferenceFile)
    i2 = Image.open(ActualFile)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
    ncomponents = i1.size[0] * i1.size[1] * 3
    if ((dif / 255.0 * 100) / ncomponents)<=tolerance:
        return True
    else:
        return False



