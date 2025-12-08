from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.wikipedia.org/")
gg=driver.find_element(by=By.XPATH,value="//input[@id='searchInput']")
gg.send_keys("selenium")
gg.submit()
wait=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//h1[@id='firstHeading']//span[@class='mw-page-title-main'][normalize-space()='Selenium']")))
assert "selenium" in driver.page_source
print("selenium is searched")

