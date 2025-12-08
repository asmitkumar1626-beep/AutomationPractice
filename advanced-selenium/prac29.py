from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("student")
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("Password123")
driver.find_element(by=By.XPATH,value="//button[@id='submit']").click()
driver.get_screenshot_as_file("ss.png")
assert "Congratulations student. You successfully logged in!" in driver.page_source
print("logged in successfully!!")
