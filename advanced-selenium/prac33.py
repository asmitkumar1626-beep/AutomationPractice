from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_forms.asp")
radio=driver.find_element(By.ID,"css")
driver.execute_script("arguments[0].scrollIntoView();",radio)
driver.execute_script("arguments[0].click();",radio)
assert radio.is_selected()
print("done nigga")
checkbox=driver.find_element(By.ID,"vehicle2")
driver.execute_script("arguments[0].scrollIntoView();",checkbox)
driver.execute_script("arguments[0].click();",checkbox)
assert checkbox.is_selected()
print("done ts too nigga")