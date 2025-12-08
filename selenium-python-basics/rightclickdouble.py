from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class right:
    def right_double(self):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        actions=ActionChains(driver)
        right_click = driver.find_element(by=By.XPATH,value="//span[@class='context-menu-one btn btn-neutral']")

        actions.move_to_element(right_click).context_click().perform()
        double_click = driver.find_element(by=By,value="//button[normalize-space()='Double-Click Me To See Alert']")
        actions.move_to_element(double_click).double_click().perform()
elm1 = right()
elm1.right_double()
