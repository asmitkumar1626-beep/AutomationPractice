from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class iframe:
     def open(self):
         driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
         iframeelement = driver.find_element(by=By.NAME,value="iframeResult")
         driver.switch_to.frame(iframeelement)
         driver.switch_to.frame(1)
         driver.find_element(by=By.XPATH,value="//body/iframe[1]").click()
         time.sleep(3)
         driver.maximize_window()


dd=iframe()
dd.open()