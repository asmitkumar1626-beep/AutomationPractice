import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class goffy:
    def screenshot(self):
        driver.get("https://www.yatra.com/")
        driver.get_screenshot_as_file(".//goffy.png")
        time.sleep(3)
        driver.find_element(by=By.XPATH,value="//div[normalize-space()='Login / Signup']").click()
        driver.get_screenshot_as_file(".//goffy1.png")
        time.sleep(3)
        driver.find_element(by=By.XPATH,value="//button[normalize-space()='Login']").click()
        driver.get_screenshot_as_file(".//goffy2.png")
        time.sleep(3)
demo_ss=goffy()
demo_ss.screenshot()
