import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)

# Open the site
driver.get("https://xhamster1.desi/best/weekly")

# Wait and click cookie/consent button if it appears
try:
    consent_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'color-brand-64d24')]"))
    )
    consent_btn.click()
except:
    print("Consent button not found or already dismissed")

# Get all links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Print their text and href
for link in links:
    text = link.text.strip()
    href = link.get_attribute("href")
    if href:  # Only show real links
        print(f"{text} -> {href}")

# Optional: close the browser
driver.quit()
