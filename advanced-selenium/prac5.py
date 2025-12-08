import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.find_element(by=By.XPATH,value="//input[1]").click()
checkbox2 = driver.find_element(by=By.XPATH,value="//form[@id='checkboxes']/input[2]")
checkbox2.click()
time.sleep(3)
if not checkbox2.is_selected():
    checkbox2.click()
time.sleep(2)
