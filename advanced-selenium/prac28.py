from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org/")
driver.find_element(by=By.XPATH,value="//input[@id='searchInput']").send_keys("Selenium (software)")
driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()
time.sleep(3)
assert "selenium" in driver.page_source
print("found selenium")
