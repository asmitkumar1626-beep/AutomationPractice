from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(by=By.XPATH,value="//input[@id='username']").send_keys("student")
driver.find_element(by=By.XPATH,value="//input[@id='password']").send_keys("Password123")
driver.find_element(by=By.XPATH,value="//button[@id='submit']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//h1[normalize-space()='Logged In Successfully']")))
assert "Congratulations student. You successfully logged in!" in driver.page_source
print("logged in!!!")
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Log out']").click()
assert "Test login" in driver.page_source
print("logged out!!")
