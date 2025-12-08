from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class Openyoutube :
    def o_pen(self):
        driver.get("https://www.youtube.com/")
        driver.find_element(by=By.XPATH,value="//input[@placeholder='Search']").send_keys("sahiba")
        driver.find_element(by=By.XPATH, value="//button[@title='Search']").click()
        time.sleep(300)
d=Openyoutube()
d.o_pen()
