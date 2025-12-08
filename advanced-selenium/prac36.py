from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_tables.asp")
gg=driver.find_elements(By.XPATH,"//table[@id='customers']//tbody//tr[3]//td[2]")
for i in gg:
    print(i.text)