from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#login
driver.get("https://www.saucedemo.com/")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Swag Labs"))
#driver.find_element(By.XPATH,"")
driver.maximize_window()
user_name=driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys("standard_user")
pass_word=driver.find_element(By.XPATH,"//input[@id='password']")
pass_word.send_keys("secret_sauce")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='login-button']"))).click()
#in the site
wait.until(EC.title_is("Swag Labs"))
#prod1
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")))
prod1 = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-backpack']")
prod1.click()
#prod2
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")))
prod2 = driver.find_element(By.XPATH,"//button[@id='add-to-cart-sauce-labs-bike-light']")
prod2.click()
#prod3
prod3 = driver.find_element(By.XPATH,"//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
driver.execute_script("arguments[0].scrollIntoView();",prod3)
prod3.click()
#cart
cart=driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
driver.execute_script("arguments[0].scrollIntoView();",cart)
cart.click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
#inside cart
checkout=driver.find_element(By.XPATH,"//button[@id='checkout']")
driver.execute_script("arguments[0].scrollIntoView();",checkout)
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@id='checkout']"))).click()
#last page
wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
name=driver.find_element(By.XPATH,"//input[@id='first-name']")
name.send_keys("asmit")
lname=driver.find_element(By.XPATH,"//input[@id='last-name']")
lname.send_keys("kanar")
zipcode=driver.find_element(By.XPATH,"//input[@id='postal-code']")
zipcode.send_keys("751016")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='continue']"))).click()
#finish
wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='title']")))
finish=driver.find_element(By.XPATH,"//button[@id='finish']")
driver.execute_script("arguments[0].scrollIntoView();",finish)
total=driver.find_element(By.XPATH,"//div[@class='summary_total_label']")
print(total.text)
finish.click()
#done
done=driver.find_element(By.XPATH,"//h2[normalize-space()='Thank you for your order!']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//h2[normalize-space()='Thank you for your order!']")))
assert "Thank you for your order!" in driver.page_source
print("ordered!!")


