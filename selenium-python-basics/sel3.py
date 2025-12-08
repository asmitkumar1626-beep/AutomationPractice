from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class openu:
    def openu1(self):
        driver.get("https://okxxx1.com/")
        b=driver.find_elements(by=By.TAG_NAME,value="a")
        print(len(b))
        for i in b:
            print(i.text)


        time.sleep(5)




d=openu()
d.openu1()