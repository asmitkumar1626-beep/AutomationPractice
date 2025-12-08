from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/")
driver.find_element(by=By.XPATH,value="//span[normalize-space()='Downloads']").click()
gg=driver.current_url
print(gg)