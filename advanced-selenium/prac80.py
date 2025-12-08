from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://okxxx1.com/")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("OK.XXX -🌶️ free porn tube!"))
gg=driver.find_elements(By.XPATH,"//div[@id='custom_list_videos_custom_videos_items']")
for i in gg:
    hh=i.find_elements(By.TAG_NAME,"a")
    for j in hh:
        print(j.text,end="|")
    print()
driver.find_element(By.XPATH,"//body/div[@class='wrapper pintour ']/div[@id='custom_list_videos_custom_videos']/div[@id='custom_list_videos_custom_videos_items']/div[4]").click()
