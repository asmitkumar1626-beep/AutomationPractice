from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
class impwait:
    def implicit(self):
        driver.get("https://login.salesforce.com/")
        driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("asmit kumar kanar")
        driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("123456789")


demo=impwait()
demo.implicit()