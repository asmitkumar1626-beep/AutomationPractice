from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver,10)
username = driver.find_element(By.XPATH,"//input[@id='user-name']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='user-name']")))
print("username is done")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
print("password done")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
print("button located")

