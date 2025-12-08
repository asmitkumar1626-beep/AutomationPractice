
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Swag Labs"))
user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys("standard_user")
pass_word=driver.find_element(By.XPATH,"//input[@id='password']")
pass_word.send_keys("secret_sauce")
submit_button=driver.find_element(By.XPATH,"//input[@id='login-button']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='login-button']")))
submit_button.click()
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
select.select_by_index(3)
add4=driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='add-to-cart-sauce-labs-onesie']")))
add4.click()
cart=driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
cart.click()
wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='title']")))
cart_items=driver.find_elements(By.XPATH,"//div[@class='cart_list']")
for i in cart_items:
    prod=i.find_elements(By.XPATH,"//div[@class='cart_item']")
    for j in prod:
        print(j.text)

wait.until(EC.presence_of_element_located((By.XPATH,"//button[@id='checkout']")))
checkout=driver.find_element(By.XPATH,"//button[@id='checkout']")
checkout.click()