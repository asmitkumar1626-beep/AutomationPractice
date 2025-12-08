from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
wait=WebDriverWait(driver,10)
#name
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='name']")))
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("asmit kumar kanar")
#email
email=driver.find_element(By.XPATH,"//input[@id='email']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='email']")))
email.send_keys("asmitkumar7750@gmai.com")
#radiobox
radiobox=driver.find_element(By.XPATH,"//body[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[2]/input[1]")
wait.until(EC.element_to_be_clickable((By.XPATH,"//body[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/div[1]/div[2]/input[1]")))
radiobox.click()
#number
number=driver.find_element(By.XPATH,"//input[@id='mobile']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='mobile']")))
number.send_keys("7873901626")
#date
date=driver.find_element(By.XPATH,"//input[@id='dob']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='dob']")))
date.send_keys("11232003")
#subjects
subjects=driver.find_element(By.XPATH,"//input[@id='subjects']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='subjects']")))
subjects.send_keys("Maths")
#checkbox
checkbox=driver.find_element(By.XPATH,"//body[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/div[1]/div[2]/input[1]")
wait.until(EC.presence_of_element_located((By.XPATH,"//body[1]/main[1]/div[1]/div[1]/div[2]/form[1]/div[7]/div[1]/div[1]/div[2]/input[1]")))
checkbox.click()
#upload
upload=driver.find_element(By.XPATH,"//input[@id='picture']")
wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='picture']")))
upload.send_keys("C:/selenium/goofy/practice/ss.png")
#address
address=driver.find_element(By.XPATH,"//textarea[@id='picture']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//textarea[@id='picture']")))
address.send_keys("metro station imran khan songs")
#dropdownstate
dropdownstate=driver.find_element(By.XPATH,"//select[@id='state']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@id='state']")))
select=Select(dropdownstate)
select.select_by_visible_text("NCR")
#dropdowncity
dropdowncity=driver.find_element(By.XPATH,"//select[@id='city']")
select1=Select(dropdowncity)
wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@id='city']")))
select1.select_by_visible_text("Lucknow")
#login
login=driver.find_element(By.XPATH,"//input[@value='Login']")
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@value='Login']")))
login.click()
print("done sir!!")
