from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com")
gg=driver.find_element(by=By.XPATH,value="//textarea[@name='q']")
gg.send_keys("selenium python")
gg.submit()
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)
assert "selenium" in driver.page_source
print("selenium is present")
