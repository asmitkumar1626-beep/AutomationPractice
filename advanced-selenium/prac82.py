import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
login=driver.find_element(By.XPATH,"//input[@id='user-name']")
login.send_keys("standard_user")
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("secret_sauce")
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='login-button']"))).click()
wait.until(EC.title_is("Swag Labs"))
driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@id='react-burger-cross-btn']").click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']"))).click()
dropdown=driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
select=Select(dropdown)
select.select_by_index(2)
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='shopping_cart_link']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='checkout']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='first-name']"))).send_keys("asmit")
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("kumar")
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("993472")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='continue']"))).click()
wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='finish']"))).click()
