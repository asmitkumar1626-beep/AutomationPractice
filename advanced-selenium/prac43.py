# Checkbox and Radio Button Selection
#
# Task: Select/deselect checkboxes and verify state
# Site: https://the-internet.herokuapp.com/checkboxes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
checkbox1=checkboxes[0]
checkbox2=checkboxes[1]
checkbox1.click()
assert checkbox1.is_selected()
print("selected")
checkbox2.click()
assert not checkbox2.is_selected()
print("unselected")

