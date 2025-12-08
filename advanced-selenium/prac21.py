from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Start']"))).click()
hellotext = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='finish']")))
assert hellotext.is_displayed()
print("done")