from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


options=Options()
options.add_argument("--guest")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.saucedemo.com/")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Swag Labs"))
username=driver.find_element(By.XPATH,"//input[@id='user-name']")
username.send_keys("standard_user")
password=driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("secret_sauce")
login=driver.find_element(By.XPATH,"//input[@id='login-button']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login-button']")))
login.click()
wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='title']")))
add1=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")))
add1.click()
add2=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")))
add2.click()
add3=driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
driver.execute_script("arguments[0].scrollIntoView();",add3)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
add3.click()
dropdown=driver.find_element(By.XPATH,"//select[@class='product_sort_container']")
select=Select(dropdown)
select.select_by_visible_text("Price (low to high)")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")))
add4=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
add4.click()
cart=driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='shopping_cart_link']")))
cart.click()
cart_prods=driver.find_elements(By.XPATH,"//div[@class='cart_list']//div[@class='inventory_item_name']")
for i in cart_prods:
    print(i.text)
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='checkout']")))
checkout=driver.find_element(By.XPATH,"//button[@id='checkout']")
checkout.click()
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='first-name']")))
first_name=driver.find_element(By.XPATH,"//input[@id='first-name']")
first_name.send_keys("Asmit")
last_name=driver.find_element(By.XPATH,"//input[@id='last-name']")
last_name.send_keys("kumar")
zip_code=driver.find_element(By.XPATH,"//input[@id='postal-code']")
zip_code.send_keys("123456")
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='continue']")))
continue_button=driver.find_element(By.XPATH,"//input[@id='continue']")
continue_button.click()
totalamnt=driver.find_element(By.XPATH,"//div[@class='summary_total_label']")
tt=totalamnt.text
print(tt)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='finish']")))
finish=driver.find_element(By.XPATH,"//button[@id='finish']")
finish.click()
wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='title']")))
assert "Thank you for your order!" in driver.page_source
print("fully automated the demosauce site!!")
driver.close()