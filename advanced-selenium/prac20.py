from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()