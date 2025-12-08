import time
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dropdown")
op1=driver.find_element(by=By.XPATH,value="//select[@id='dropdown']")
gg=Select(op1)
gg.select_by_index(1)
selected= Select.first_selected_option
print(selected)