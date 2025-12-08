from asyncio import set_child_watcher

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(by=By.XPATH,value="//a[normalize-space()='Click Here']").click()
originalwindow=driver.current_window_handle
for windowhandle in driver.window_handles:
    if windowhandle != originalwindow:
        driver.switch_to.window(windowhandle)
gg=driver.find_element(by=By.TAG_NAME,value="h3")
print(gg.text)
driver.switch_to.window(originalwindow)
print("done")