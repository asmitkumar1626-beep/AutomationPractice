from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.yatra.com")
driver.find_element(by=By.ID,value="mobile-number").send_keys("9937148895")
