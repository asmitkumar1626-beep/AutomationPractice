from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_tables.asp")
table = driver.find_elements(By.XPATH,"//table[@id='customers']//tr")[1:]
for i in table:
    cells=i.find_elements(By.TAG_NAME,"td")
    if cells:
        print(cells[0].text,"-",cells[1].text,"-",cells[2].text)