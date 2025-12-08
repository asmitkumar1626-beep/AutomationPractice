import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown  = driver.find_element(by=By.XPATH,value="//select[@id='dropdown']")
select=Select(dropdown)
time.sleep(2)
select.select_by_index(2)
time.sleep(3)