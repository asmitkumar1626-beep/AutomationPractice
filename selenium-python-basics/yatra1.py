from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class openyatra:
    def open(self):
        driver.get("https://www.youtube.com/")
        driver.find_element(by=By.NAME,value="search_query").send_keys("sahiba")
        driver.find_element(by=By.XPATH, value="//button[@title='Search']").click()
        time.sleep(7)
call=openyatra()
call.open()