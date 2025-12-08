from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
wait=WebDriverWait(driver,10)
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Alert']").click()
driver.switch_to.alert.accept()
assert "You successfully clicked an alert" in driver.page_source
print("You successfully clicked an alert")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Confirm']").click()
driver.switch_to.alert.accept()
assert "You clicked: Ok" in driver.page_source
print("You clicked: Ok")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Prompt']").click()
gg=driver.switch_to.alert
gg.send_keys("asmit")
gg.accept()
assert "You entered: asmit" in driver.page_source
print("You entered: asmit")