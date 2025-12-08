import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Start']").click()
a=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"finish")))
time.sleep(3)
print(a.text)