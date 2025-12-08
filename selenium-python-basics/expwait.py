from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class expwait:
    def demo_exp(self):
        driver.get("https://www.yatra.com/")
        wait=WebDriverWait(driver,10)
        driver.find_element(by=By.XPATH,value="//div[normalize-space()='Login / Signup']").click()
        driver.find_element(by=By.XPATH,value="//input[@id='mobile-number']").send_keys("9937148895")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Login']"))).click()

waitex=expwait()
waitex.demo_exp()