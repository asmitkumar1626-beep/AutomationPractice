import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
elm1 = driver.find_element(by=By.XPATH,value="//div[@id='column-a']")
elm2 = driver.find_element(by=By.XPATH,value="//div[@id='column-b']")
action=ActionChains(driver)
action.drag_and_drop(elm1,elm2).perform()
elm1text=driver.find_element(by=By.XPATH,value="//header[normalize-space()='A']").text
elm2text=driver.find_element(by=By.XPATH,value="//header[normalize-space()='B']").text
print(elm1text)
# assert elm1text=="B"
# print("ur work is done")
time.sleep(3)

