from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
driver.switch_to.frame("iframeResult")
dropdown = driver.find_element(by=By.XPATH,value="//*[@id='cars']")
select=Select(dropdown)
select.select_by_visible_text("Saab")
nigga=select.first_selected_option.text
assert "Saab"==nigga
print("done!")