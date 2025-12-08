from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Define path to chromedriver
service = Service("C:\\chromedriver\\chromedriver.exe")

# Launch Chrome without custom options
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.maximize_window()
driver.get("https://www.google.com")
print(driver.title)
driver.close()

