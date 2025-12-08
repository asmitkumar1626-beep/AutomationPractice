# Checkbox and Radio Button Selection
# Task: Select/deselect checkboxes and verify state
# Site: https://the-internet.herokuapp.com/checkboxes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown= driver.find_element(by=By.XPATH,value="//select[@id='dropdown']")
select=Select(dropdown)
select.select_by_index(2)
print(select.first_selected_option.text)

