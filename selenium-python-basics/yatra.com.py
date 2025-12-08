
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class openyatra:
    def emailtype(self):
        driver.get("https://www.yatra.com/")
        driver.find_element(by=By.ID,value=("mobile-number")).send_keys("asmitkumar7750@gmail.com")
        time.sleep(4)

open=openyatra()
open.emailtype()


