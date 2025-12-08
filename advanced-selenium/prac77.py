from selenium  import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
gg=driver.find_element(By.XPATH,"//button[normalize-space()='Start']")
gg.click()
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[normalize-space()='Hello World!']")))
print("hello world")