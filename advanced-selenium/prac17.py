from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(by=By.XPATH,value="//input[@name='username']").send_keys("student")
driver.find_element(by=By.XPATH,value="//input[@name='password']").send_keys("asmit")
driver.find_element(by=By.XPATH,value="//button[@id='submit']").click()
assert "Your password is invalid!" in driver.page_source
print("wrong password")
