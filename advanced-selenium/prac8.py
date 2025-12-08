import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Alert']").click()
WebDriverWait(driver,10).until(EC.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(3)

