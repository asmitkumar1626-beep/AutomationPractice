import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
wait=WebDriverWait(driver,10)
actions=ActionChains(driver)
acnts=driver.find_element(By.XPATH,"//span[normalize-space()='Account & Lists']")
actions.move_to_element(acnts).perform()
wait.until(EC.presence_of_element_located((By.XPATH," //span[@class='nav-action-inner']")))
signin=driver.find_element(By.XPATH," //span[@class='nav-action-inner']")
signin.click()
time.sleep(3)