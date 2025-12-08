from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("student")
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("Password123")
driver.find_element(by=By.XPATH,value="//button[@id='submit']").click()
gg=driver.current_url
print(gg)
assert gg=="https://practicetestautomation.com/logged-in-successfully/"
print("logged in")
