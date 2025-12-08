from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.wikipedia.org")
gg=driver.find_element(by=By.XPATH,value="//input[@name='search']")
gg.send_keys("Python (programming language)")
driver.find_element(by=By.XPATH,value="//i[@class='sprite svg-search-icon']").click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Python (programming language)")))
assert "python" in driver.page_source
print("python is present")