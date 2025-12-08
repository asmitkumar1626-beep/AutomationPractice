import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://letcode.in/table")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("WebTable | LetCode with Koushik"))
tab=driver.find_elements(By.XPATH,"//table[@id='simpletable']//tbody//tr")
for i in tab:
    name=i.find_element(By.XPATH,"./td[1]").text
    if name=="Yashwanth":
        i.find_element(By.XPATH,"./td[4]//input[@type='checkbox']").click()
