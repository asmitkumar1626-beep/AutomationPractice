from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))


class yatra:
    def opeya(self):

        driver.get("https://www.yatra.com/hotels")
        driver.find_element(by=By.XPATH,value="/html/body/main/div/main/div[1]/div/div[3]/div/div[3]/button/div/div/div/p").click()
        a=driver.find_element(by=By.XPATH,value="/html/body/main/div/main/div[1]/div/div[3]/div/div[3]/div/div/div[1]").is_displayed()
        print(a)
        driver.find_element(by=By.XPATH,value="/html/body/main/div/main/div[1]/div/div[3]/div/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/button[2]").click()
        b=driver.find_element(by=By.XPATH,value="/html/body/main/div/main/div[1]/div/div[3]/div/div[3]/div/div/div[1]/div[3]/div/h5").is_displayed()
        print(b)
demo=yatra()
demo.opeya()
