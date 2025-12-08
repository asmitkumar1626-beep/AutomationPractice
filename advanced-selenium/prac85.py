from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import csv
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://letcode.in/table")
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("WebTable | LetCode with Koushik"))
table_date=driver.find_elements(By.XPATH,"//table[@class='mat-sort table is-bordered is-striped is-narrow is-hoverable is-fullwidth']//thead//tr")
headers = []
for i in table_date:
    cols=i.find_elements(By.TAG_NAME,"th")
    for j in cols:
        headers.append(j.text)
    print("|" .join(headers))


file=open("table_output.csv","w",newline="",encoding="utf-8")
writer = csv.writer(file)
writer.writerow(headers)

tbody_data = driver.find_elements(By.XPATH, "//table[@class='mat-sort table is-bordered is-striped is-narrow is-hoverable is-fullwidth']//tbody//tr")

for row in tbody_data:
    row_values = []
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
        row_values.append(col.text)

    print(" | ".join(row_values))

    writer.writerow(row_values)

file.close()
