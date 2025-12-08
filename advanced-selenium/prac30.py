from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")
gg=driver.find_elements(by=By.XPATH,value="//div[@class='medium-widget event-widget last']//li")
for i in gg:
    print(i.text)