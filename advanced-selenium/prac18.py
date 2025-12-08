from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
driver.switch_to.frame("iframeResult")
gg = driver.find_element(by=By.XPATH,value="//select[@name='cars']")
select=Select(gg)
select.select_by_visible_text("Saab")
selectedoption=select.first_selected_option.text
assert selectedoption=="Saab"
print("Saab selected")