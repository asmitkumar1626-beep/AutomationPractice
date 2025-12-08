import time

from selenium  import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/login")
driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("asmit")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("asmit123")
wait= WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='login']")))
click=driver.find_element(By.XPATH,"//button[@id='login']").click()
time.sleep(5)
assert "Invalid username or password!" in driver.page_source
print("wrong password")

