import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("okxxx")
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").submit()
time.sleep(2)
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("okxxx - Google Search"))
link1=driver.find_elements(By.XPATH,"//div[@class='eKjLze']")
for i in link1:
    i.find_element(By.TAG_NAME,"a").click()
wait.until(EC.title_is("OK.XXX -🌶️ free porn tube!"))
links=driver.find_elements(By.XPATH,"//div[@id='custom_list_videos_custom_videos_items']")
for i in links:
    link=i.find_elements(By.TAG_NAME,"a")
    for j in link:
        print(j.text)
print("all videos names printed")
