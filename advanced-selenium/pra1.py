from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")
gg=driver.title
print(gg)