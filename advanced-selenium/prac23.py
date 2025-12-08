import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/hovers")
action=ActionChains(driver)
image=driver.find_element(by=By.XPATH,value="//div[@class='example']//div[1]//img[1]")
action.move_to_element(image).perform()
assert "name: user1" in driver.page_source
print("its there boss")

