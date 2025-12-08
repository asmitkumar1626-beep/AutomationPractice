from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class alerts:
    def handlealerts(self):
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.switch_to.frame(driver.find_element(by=By.XPATH,value="//iframe[@id='iframeResult']"))
        driver.find_element(by=By.XPATH,value="/html/body/button").click()
        driver.switch_to.alert.accept()
        time.sleep(5)

demo=alerts()
demo.handlealerts()
