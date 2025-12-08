from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/checkbox")
driver.find_element(by=By.XPATH,value="//button[@title='Expand all']").click()
driver.find_element(by=By.XPATH,value="//label[@for='tree-node-workspace']//span[@class='rct-checkbox']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='You have selected :']")))
assert all(x in driver.page_source for x in ["veu","react","angular"])
print("done")
