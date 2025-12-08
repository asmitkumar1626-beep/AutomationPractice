import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://xhamster1.desi/best/weekly")
gg=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(@class, 'color-brand-64d24')]")))
gg.click()
results = driver.find_elements(by=By.TAG_NAME,value="a")
for i in results :
    print(i.text)


