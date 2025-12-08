from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_tables.asp")
wait = WebDriverWait(driver,10)
wait.until(EC.title_is("HTML Tables"))
tr = driver.find_elements(By.XPATH,"//table[@id='customers']//tbody//tr[2]")
for i in tr:
    td=i.find_elements(By.TAG_NAME,"td")
    print(len(td))

# for i in tr:
#     td = i.find_elements(By.TAG_NAME, "td")
#     for j in td:
#         print(j.text,end="|")
#     print()
