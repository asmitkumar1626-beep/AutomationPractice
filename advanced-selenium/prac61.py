import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://automationexercise.com/products")
element=driver.find_element(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/ul[1]/li[1]/a[1]")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.find_element(By.XPATH,"//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/a[1]").click()
wait=WebDriverWait(driver,10)
continuebtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Continue Shopping']")))
continuebtn.click()
time.sleep(2)
item2=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='5']")))
item2.click()

continuebtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Continue Shopping']")))
continuebtn.click()
time.sleep(2)
item3=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@data-product-id='6']")))
item3.click()
cartbtn=wait.until(EC.element_to_be_clickable((By.XPATH,"//u[normalize-space()='View Cart']")))
cartbtn.click()
time.sleep(2)
list1 = driver.find_elements(By.XPATH,"//tbody//tr")

for i in list1:
    print(i)

    


time.sleep(4)