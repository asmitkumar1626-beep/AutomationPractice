from selenium import webdriver
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practice.expandtesting.com/login")
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys("practice")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']"))).send_keys("<PASSWORD>")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='submit-login']"))).click()
assert "Your password is invalid!" in driver.page_source
print("invalid password")