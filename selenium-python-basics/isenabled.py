from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
class daru:
    def openu(self):
        driver.get("https://training.openspan.com/login")
        driver.find_element(by=By.XPATH,value="//input[@id='user_name']").send_keys("testing")
        driver.find_element(by=By.XPATH,value="//input[@id='user_pass']").send_keys("jigolo")
        nibba=driver.find_element(by=By.XPATH,value="//input[@id='login_button']").is_enabled()
        print(nibba)
demo=daru()
demo.openu()
