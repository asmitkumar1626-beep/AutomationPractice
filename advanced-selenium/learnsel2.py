from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
driver.find_element(By.XPATH,"//*[@id='center']/yt-searchbox/div[1]/form/input").send_keys("weekend")
driver.find_element(By.XPATH,"//*[@id='center']/yt-searchbox/button").click()
time.sleep(4)
driver.find_element(by=By.ID,value="video-title").click()
time.sleep(5)
