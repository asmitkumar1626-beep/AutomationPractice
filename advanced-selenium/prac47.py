from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.switch_to.frame("iframeResult")
gg=driver.find_element(by=By.TAG_NAME,value="p")
print(gg.text)
assert gg.text == "An iframe is used to display a web page within a web page:"
print('JOB DONE!!')
