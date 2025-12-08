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
driver.find_element(by=By.XPATH,value="//textarea[@id='APjFqb']").send_keys("https://automationexercise.com/")
driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[2]/div[4]/form[1]/div[1]/div[1]/div[3]/center[1]/input[1]").click()
driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[3]/div[1]/div[12]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]/div[1]/div[1]/div[1]/div[2]/cite[1]").click()
wait=WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='item active']//span[1]")))
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Signup / Login']").click()
driver.find_element(by=By.XPATH,value="//input[@placeholder='Name']").send_keys("asmit")
driver.find_element(by=By.XPATH,value="//input[@data-qa='signup-email']").send_keys("asmitkumar7750@gmail.com")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Signup']").click()
wait.until(EC.presence_of_element_located((By.XPATH,"//b[normalize-space()='Enter Account Information']")))
driver.find_element(by=By.XPATH,value="//input[@id='id_gender1']").click()
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("asmit123")
dropdown=driver.find_element(by=By.XPATH,value="//select[@id='days']")
dropdown2=driver.find_element(by=By.XPATH,value="//select[@id='months']")
dropdown3=driver.find_element(by=By.XPATH,value="//select[@id='years']")
select=Select(dropdown)
select.select_by_index(9)
select2=Select(dropdown2)
select2.select_by_index(4)
select3=Select(dropdown3)
select3.select_by_index(3)
driver.find_element(by=By.XPATH,value="//input[@id='newsletter']").click()
driver.find_element(by=By.XPATH,value="//input[@id='optin']").click()
driver.find_element(by=By.XPATH,value="//input[@id='first_name']").send_keys("asmit")
driver.find_element(by=By.XPATH,value="//input[@id='last_name']").send_keys("kumar")
driver.find_element(by=By.XPATH,value="//input[@id='company']").send_keys("google")
driver.find_element(by=By.XPATH,value="//input[@id='address1']").send_keys("MIG1 15/9 BDA COLONY")
driver.find_element(by=By.XPATH,value="//input[@id='address2']").send_keys("MIG 2 10/2 BDA COLONY")
country_dropdown=driver.find_element(by=By.XPATH,value="//select[@id='country']")
select4=Select(country_dropdown)
select4.select_by_index(3)
driver.find_element(by=By.XPATH,value="//input[@id='state']").send_keys("odisha")
driver.find_element(by=By.XPATH,value="//input[@id='city']").send_keys("bhubaneswar")
driver.find_element(by=By.XPATH,value="//input[@id='zipcode']").send_keys("751016")
driver.find_element(by=By.XPATH,value="//input[@id='mobile_number']").send_keys("7873901626")
driver.find_element(by=By.XPATH,value="//button[normalize-space()='Create Account']").click()
time.sleep(5)
# driver.find_element(by=By.XPATH,value="")
# driver.find_element(by=By.XPATH,value="")
# driver.find_element(by=By.XPATH,value="")













