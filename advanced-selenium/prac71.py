from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Swag Labs"))
username=driver.find_element(By.XPATH,"//input[@id='user-name']")
password=driver.find_element(By.XPATH,"//input[@id='password']")
button=driver.find_element(By.XPATH,"//input[@id='login-button']")
username.send_keys("locked_out_user")
password.send_keys("secret_sauce")
button.click()
print("done")
