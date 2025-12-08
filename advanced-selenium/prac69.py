from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/?zx=1763558738455&no_sw_cr=1")
gg=driver.title
assert "Google" == gg
print("its google")
