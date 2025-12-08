from selenium import webdriver
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class drop:
    def dropdown(self):
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/signup/sales-ee/?d=topnav2-btn-ft")
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[1]/div[3]/div/input").send_keys("gungun")
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[1]/div[4]/div/input").send_keys("kumar")
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[1]/div[5]/div/input").send_keys("jigollo")
        driver.find_element(by=By.XPATH,value="//a[@data-page-cntrl='next']").click()
        dome=driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[2]/div/select")
        dd=Select(dome)
        dd.select_by_index(1)
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/div/input").send_keys("giligiligili")
        dome2=driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[4]/div[1]/div/div/select")
        cc=Select(dome2)
        cc.select_by_index(6)
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[4]/div[1]/div[2]/a").click()
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[3]/div[2]/div/input").send_keys("9937148895")
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[3]/div[3]/div/input").send_keys("asmitkumar7750@gmail.com")
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[3]/div[4]/div/div/div[1]").click()
        driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[1]/div/div[6]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/form/div[4]/div[1]/div[3]/button").click()
        time.sleep(5)
v=drop()
v.dropdown()