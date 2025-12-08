from charset_normalizer import from_path
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Start']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,"finish")))
assert "Hello World!" in driver.page_source
print("performed")