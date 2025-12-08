import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options = options)
driver.get("https://www.google.com/")
gg=driver.find_element(by=By.XPATH,value="//textarea[@id='APjFqb']")
gg.send_keys("https://automationexercise.com/")
gg.submit()
time.sleep(2)
driver.find_element(by=By.XPATH,value="//h3[contains(text(),'Automation Exercise')]").click()
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='item active']//span[1]")))
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Signup / Login']").click()
driver.find_element(by=By.XPATH,value="//input[@data-qa='login-email']").send_keys("asmitkumar7750@gmail.com")
driver.find_element(by=By.XPATH,value="//input[@placeholder='Password']").send_keys("asmit123")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Login']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='item active']//span[1]")))
driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[1]").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//h4[normalize-space()='Added!']")))
wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Continue Shopping']")))
cn=driver.find_element(by=By.XPATH,value="//button[normalize-space()='Continue Shopping']")
cn.click()
driver.find_element(By.XPATH, "(//a[contains(text(),'Add to cart')])[2]").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//h4[normalize-space()='Added!']")))
driver.find_element(by=By.XPATH,value="//u[normalize-space()='View Cart']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//li[@class='active']")))
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Proceed To Checkout']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//h2[normalize-space()='Address Details']")))
driver.find_element(by=By.XPATH,value="//textarea[@name='message']").send_keys("you guys are awesome loved the ui")
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Place Order']").click()
driver.find_element(by=By.XPATH,value="//input[@name='name_on_card']").send_keys("asmit kumar kanar")
driver.find_element(by=By.XPATH,value="//input[@name='card_number']").send_keys("194565461235")
driver.find_element(by=By.XPATH,value="//input[@placeholder='ex. 311']").send_keys("654")
driver.find_element(by=By.XPATH,value="//input[@placeholder='MM']").send_keys("02")
driver.find_element(by=By.XPATH,value="//input[@placeholder='YYYY']").send_keys("2030")
driver.find_element(by=By.XPATH,value="//button[@id='submit']").click()
assert "Order Placed!" in driver.page_source
print("order placed!!")







