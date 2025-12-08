from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Alert']").click()
gg=driver.switch_to.alert
gg.accept()
print("executed one")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Confirm']").click()
nn=driver.switch_to.alert
nn.accept()
print("executed two")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Click for JS Prompt']").click()
ff=driver.switch_to.alert
ff.send_keys("asmit")
ff.accept()
print("executed 3")
