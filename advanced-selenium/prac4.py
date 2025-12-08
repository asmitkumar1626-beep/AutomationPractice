from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/")
gg = driver.find_elements(by=By.TAG_NAME,value="a")
for i in gg:
    print(i.text)