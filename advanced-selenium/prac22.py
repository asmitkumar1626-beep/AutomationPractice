import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(by=By.XPATH,value="//input[@id='file-upload']").send_keys("C:/selenium/goofy/check.py")
driver.find_element(by=By.XPATH,value="//input[@id='file-submit']").click()
time.sleep(3)

assert "checkbox.py" in driver.page_source
print("yes its there")