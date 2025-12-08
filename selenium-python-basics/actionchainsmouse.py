from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class Action:
    def mouse(self):
        driver.get("https://www.yatra.com/offer/details/american-express-network-card-offers")
        actions=ActionChains(driver)
        actions.move_to_element(driver.find_element(by=By.XPATH,value="//a[@class='dropdown-toggle'][normalize-space()='Support']")).perform()
        driver.find_element(by=By.XPATH,value='//*[@id="customer_support_ddn"]/ul/li[4]/a').click()
demo=Action()
demo.mouse()

