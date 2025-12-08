# 6. File Upload Automation
# Task: Upload a local file and verify result
# Site: https://the-internet.herokuapp.com/upload
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/upload")
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='file-upload']"))).send_keys("C:/selenium/goofy/practice/prac44.py")
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
assert "File Uploaded!" in driver.page_source
print("File Uploaded!")

