from optparse import Option

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options= Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("ranbir kapoor")
driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/form/div[1]/div[1]/div[3]/center/input[1]").click()
time.sleep(3)



