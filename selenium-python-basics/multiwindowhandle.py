from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.yatra.com/")
windowhandle = driver.current_window_handle
print(windowhandle)
driver.find_element(by=By.XPATH,value="//span[contains(text(),'*Offer Valid on American Express Network Card Tran')]").click()
driver.find_element(by=By.XPATH,value="//input[@id='BE_flight_origin_city']").send_keys("hello")
 