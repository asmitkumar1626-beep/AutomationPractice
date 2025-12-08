from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class slider:
    def sliders_open(self):
        driver.get("https://www.snapdeal.com/")
        driver.maximize_window()
        actions=ActionChains(driver)
        mobile_electronics=driver.find_element(by=By.XPATH,value="//span[normalize-space()='Mobile & Accessories']")
        actions.move_to_element(mobile_electronics).click().perform()
        time.sleep(3)
        screen_guard=driver.find_element(by=By.XPATH,value="//span[normalize-space()='Screen Guards']")
        actions.move_to_element(screen_guard).click().perform()
        el1=driver.find_element(by=By.XPATH,value="//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        el2=driver.find_element(by=By.XPATH,value="//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        actions.drag_and_drop_by_offset(el1,60,0).perform()
        time.sleep(2)
        actions.click_and_hold(el2).pause(1).move_by_offset(-20,0).release().perform()
elm1=slider()
elm1.sliders_open()