from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://testautomationpractice.blogspot.com/")
driver.execute_script("window.scrollTo(0,600);")
time.sleep(4)

checkboxes=driver.find_elements(by=By.XPATH,value="//input[@type='checkbox']")
for checkbox in checkboxes:
    checkbox.click()