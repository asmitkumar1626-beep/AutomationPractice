import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/howto/howto_css_dropdown.asp")
menu=driver.find_element(By.XPATH,"//button[normalize-space()='Hover Me']")
wait =   WebDriverWait(driver,10)
actions=ActionChains(driver)
actions.move_to_element(menu).perform()
wait.until(EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Link 2']")))
print("present")
