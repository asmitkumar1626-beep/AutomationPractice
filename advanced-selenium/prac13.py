from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/upload")
input_file=driver.find_element(by=By.XPATH,value="//input[@id='file-upload']")
input_file.send_keys("C:\selenium\goofy\practice\prac2.py")
driver.find_element(by=By.XPATH,value="//input[@id='file-submit']").click()