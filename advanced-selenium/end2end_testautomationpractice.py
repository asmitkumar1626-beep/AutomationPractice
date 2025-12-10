
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import csv
options=Options()
options.add_argument("--guest")
options.add_argument("--disable-blink-features=AutomationControlled")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(EC.title_is("Automation Testing Practice"))
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='name']")))
name=driver.find_element(By.XPATH,"//input[@id='name']")
name.send_keys("asmit")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='email']")))
email=driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("asmitkumar7750@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='phone']")))
num=driver.find_element(By.XPATH,"//input[@id='phone']")
num.send_keys("9937148895")
wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@id='textarea']"))).send_keys("MIG-1 15/9 BBSR BDA COLONY")
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='male']")))
radio_butt=driver.find_element(By.XPATH,"//input[@id='male']")
radio_butt.click()
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='sunday']")))
checkbox_sunday=driver.find_element(By.XPATH,"//input[@id='sunday']")
checkbox_sunday.click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='tuesday']")))
checkbox_tuesday=driver.find_element(By.XPATH,"//input[@id='tuesday']")
checkbox_tuesday.click()
dropdown=driver.find_element(By.XPATH,"//select[@id='country']")
select=Select(dropdown)
select.select_by_visible_text("Australia")
scroll_dropdown=driver.find_element(By.XPATH,"//select[@id='colors']")
select2=Select(scroll_dropdown)
select2.select_by_visible_text("Green")
sortedlist=driver.find_elements(By.XPATH,"//select[@id='animals']//option")
for i in sortedlist:
    if i.text == "Rabbit":
        i.click()
date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='datepicker']")))
date.send_keys("03/20/2003")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='txtDate']"))).send_keys("20/03/2003")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='start-date']"))).send_keys("03/20/2003")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='end-date']"))).send_keys("03/25/2020")
submit=driver.find_element(By.XPATH,"//button[@class='submit-btn']")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='submit-btn']")))
submit.click()
driver.find_element(By.XPATH,"//input[@id='singleFileInput']").send_keys("C:/selenium/goofy/practice/ss.png")
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Upload Single File']"))).click()
table_row=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr")
headers=[]
for i in table_row:
    table_col=i.find_elements(By.TAG_NAME,"td")
    for col in table_col:
        headers.append(col.text)
        print(col.text,end="|")
    print()
file=open("table_outputt.csv","w",newline="",encoding="utf-8")
writer=csv.writer(file)
writer.writerow(headers)
simplealert=driver.find_element(By.XPATH,"//button[@id='alertBtn']")
driver.execute_script("arguments[0].scrollIntoView();",simplealert)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='alertBtn']")))
simplealert.click()
driver.switch_to.alert.accept()
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='confirmBtn']"))).click()
driver.switch_to.alert.dismiss()
actions=ActionChains(driver)
point_at_me=driver.find_element(By.XPATH,"//button[normalize-space()='Point Me']")
actions.move_to_element(point_at_me).perform()
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Mobiles']"))).click()
double_click=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
actions.double_click(double_click).perform()
source=driver.find_element(By.XPATH,"//div[@id='draggable']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
actions.drag_and_drop(source, target).perform()
slider=driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
actions.drag_and_drop_by_offset(slider,40,0).perform()
scroll_dropdown_2=driver.find_element(By.XPATH,"//input[@id='comboBox']")
actions.move_to_element(scroll_dropdown_2).click().perform()
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='dropdown']")))
dropdownn=driver.find_elements(By.XPATH,"//div[@id='dropdown']//div[@class='option']")
for i in dropdownn:
    if i.text =="Item 2":
        i.click()
print("end to end automation is done!!")










