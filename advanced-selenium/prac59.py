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
driver.get("https://www.google.com/")
driver.find_element(by=By.XPATH,value="//textarea[@id='APjFqb']").send_keys("selenium")
wait=WebDriverWait(driver,10)
suggestions = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@id='Alh6id']//li")))
print("3rd suggestion is",suggestions[2].text)
suggestions[2].click()
wait.until(EC.presence_of_element_located((By.ID,"search")))
assert "selenium sulfide shampoo" in driver.page_source.lower()
print("work done!!")
