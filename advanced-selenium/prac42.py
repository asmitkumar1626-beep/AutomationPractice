from multiprocessing.context import assert_spawning

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
driver.find_element(by=By.XPATH,value="//input[@type='checkbox']").click()
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Remove']").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//p[@id='message']")))
assert "It's gone!" in driver.page_source
print("process successful!")
enablebtn=driver.find_element(by=By.XPATH,value="//button[normalize-space()='Enable']").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//p[@id='message']")))
assert "It's enabled!" in driver.page_source
print("done boss!!")
driver.quit()
