import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# ---------------------- SETUP ----------------------
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

driver.maximize_window()
driver.get("https://automationexercise.com/")


# ---------------------- HELPER FUNCTIONS ----------------------
def remove_ads():
    """Remove all ad iframes that block clicking."""
    driver.execute_script("""
        let iframes = document.querySelectorAll("iframe");
        iframes.forEach(f => f.remove());
    """)


def safe_click(xpath):
    """Wait → scroll → JS click (most reliable)."""
    remove_ads()
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.7)
    driver.execute_script("arguments[0].click();", element)


# ---------------------- LOGIN ----------------------
safe_click("//a[normalize-space()='Signup / Login']")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-qa='login-email']")))
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("asmitkumar7750@gmail.com")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("asmit123")

safe_click("//button[normalize-space()='Login']")


# ---------------------- ADD TO CART (2 products) ----------------------
safe_click("(//a[contains(text(),'Add to cart')])[1]")
wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Added!']")))
safe_click("//button[normalize-space()='Continue Shopping']")

safe_click("(//a[contains(text(),'Add to cart')])[2]")
wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Added!']")))

safe_click("//u[normalize-space()='View Cart']")


# ---------------------- CHECKOUT ----------------------
wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@class='active']")))
safe_click("//a[normalize-space()='Proceed To Checkout']")

wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='Address Details']")))

driver.find_element(By.XPATH, "//textarea[@name='message']").send_keys(
    "you guys are awesome loved the UI!"
)

safe_click("//a[normalize-space()='Place Order']")


# ---------------------- PAYMENT ----------------------
driver.find_element(By.NAME, "name_on_card").send_keys("Asmit Kumar Kanar")
driver.find_element(By.NAME, "card_number").send_keys("194565461235")
driver.find_element(By.XPATH, "//input[@placeholder='ex. 311']").send_keys("654")
driver.find_element(By.XPATH, "//input[@placeholder='MM']").send_keys("02")
driver.find_element(By.XPATH, "//input[@placeholder='YYYY']").send_keys("2030")

safe_click("//button[@id='submit']")


# ---------------------- CONFIRMATION ----------------------
assert "Order Placed!" in driver.page_source
print("🎉 ORDER PLACED SUCCESSFULLY!")


driver.quit()
