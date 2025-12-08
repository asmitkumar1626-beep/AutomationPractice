from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Form Authentication']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Login Page']")))
assert "Login Page" in driver.page_source
print("in log in page")