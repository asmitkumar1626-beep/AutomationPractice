import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://scrollmagic.io/examples/advanced/infinite_scrolling.html")

# Start with empty list
boxes = []

# Scroll until at least 20 boxes are loaded
while len(boxes) < 20:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for new boxes to load
    # Update boxes list
    boxes = driver.find_elements(By.CSS_SELECTOR, ".box")
    print(f"Boxes loaded: {len(boxes)}")

print(f"Final number of boxes loaded: {len(boxes)}")

# Assertion
assert len(boxes) >= 20, "Less than 20 boxes loaded!"

driver.quit()

