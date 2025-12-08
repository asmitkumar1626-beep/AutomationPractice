import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_forms.asp")
driver.maximize_window()
radio = driver.find_element(by=By.XPATH,value="//input[@id='css']")
driver.execute_script("arguments[0].scrollIntoView();",radio)
driver.execute_script("arguments[0].click();",radio)
assert radio.is_selected()
print("it worked")

checkbox= driver.find_element(by=By.XPATH,value="//input[@id='vehicle2']")
driver.execute_script("arguments[0].scrollIntoView();",checkbox)
driver.execute_script("arguments[0].click();",checkbox)
assert checkbox.is_selected()
print("it also worked")
time.sleep(3)





