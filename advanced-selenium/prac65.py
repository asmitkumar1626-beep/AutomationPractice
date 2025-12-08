import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Simple Context Menu"))
actions=ActionChains(driver)
rightclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
actions.context_click(rightclick).perform()
wait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Quit']")))
quit=driver.find_element(By.XPATH,"//span[text()='Quit']")
quit.click()
alert=driver.switch_to.alert
alert.accept()
wait.until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")))
dc=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
actions.double_click(dc).perform()
alert2=driver.switch_to.alert
alert2.accept()