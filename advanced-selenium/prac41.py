from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("tomsmith")
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("SuperSecretPassword!")
driver.find_element(by=By.XPATH,value="//i[@class='fa fa-2x fa-sign-in']").click()
assert "success" in driver.page_source
print("logged in")