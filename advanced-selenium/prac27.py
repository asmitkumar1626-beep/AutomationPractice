import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com")
gg=driver.find_element(by=By.XPATH,value="//textarea[@name='q']")
gg.send_keys("selenium python")
gg.submit()
time.sleep(3)

