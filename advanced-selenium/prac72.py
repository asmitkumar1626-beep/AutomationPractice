from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/")
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/downloads']")))
nav=driver.find_elements(By.XPATH,"//ul[@class='navbar-nav mr-4 mb-2 mb-lg-0 ps-4 ps-lg-2']//li")
for i in nav:
    print(i.text)