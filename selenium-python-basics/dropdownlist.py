from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.ie.service import Service
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.yatra.com/")
goingto = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/p[2]")
goingto.click()
goingto.send_keys("New")

