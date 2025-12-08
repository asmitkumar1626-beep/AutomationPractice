import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("tomsmith")
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("SuperSecretPassword!")
gg=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='radius']")))
gg.click()
driver.get_screenshot_as_file("screenshot.png")


time.sleep(3)