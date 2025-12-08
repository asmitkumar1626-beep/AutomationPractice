from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
wait.until(EC.title_is("Swag Labs"))
username=driver.find_element(By.XPATH,"//input[@id='user-name']")
username.send_keys("standard_user")
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("secret_sauce")
submit=driver.find_element(By.XPATH,"//input[@id='login-button']")
submit.click()
wait.until(EC.title_is("Swag Labs"))
wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='react-burger-menu-btn']")))
click_settings=driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']")
click_settings.click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='react-burger-cross-btn']")))
cross_button=driver.find_element(By.XPATH,"//button[@id='react-burger-cross-btn']")
cross_button.click()
dropdown=driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
select=Select(dropdown)
select.select_by_index(3)
add1=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
add1.click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']"))).click()
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='remove-sauce-labs-fleece-jacket']")))
remove=driver.find_element(By.XPATH,"//button[@id='remove-sauce-labs-fleece-jacket']")
remove.click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='checkout']"))).click()
time.slee
print("gone well so far")
