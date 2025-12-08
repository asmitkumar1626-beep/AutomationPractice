from selenium  import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/html_tables.asp")
gg=driver.find_elements(By.XPATH,"//table[@id = 'customers']//tbody//tr")
print(len(gg))
hh=driver.find_elements(By.XPATH,"//table[@id = 'customers']//tbody//tr//th")
print(len(hh))
