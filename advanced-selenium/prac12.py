from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/tables")
tabledata=driver.find_elements(by=By.XPATH,value="//table[1]/tbody/tr")
for i in tabledata:
    print(i.text)