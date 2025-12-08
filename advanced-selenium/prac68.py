import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("")
driver.find_element(By.XPATH,"")
wait =   WebDriverWait(driver,10)
actions=ActionChains(driver)
