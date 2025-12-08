from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class checkbox:
    def check(self):
        driver.get("https://www.sugarcrm.com/request-demo/")
        driver.find_element(by=By.ID,value="input_1_1").send_keys("testing@gmail.com")
        driver.find_element(by=By.ID, value="input_1_3_3").send_keys("asmit kumar kanar")
        driver.find_element(by=By.ID, value="input_1_3_6").send_keys("nonya")
        driver.find_element(by=By.ID, value="input_1_4").send_keys("9937148895")
        driver.find_element(by=By.ID, value="input_1_5").send_keys("automation tester")
        driver.find_element(by=By.ID, value="input_1_6").send_keys("Google")
        driver.find_element(by=By.XPATH, value="//label[contains(text(),'I would like to receive information, tips, and off')]").click()
demo=checkbox()
demo.check()