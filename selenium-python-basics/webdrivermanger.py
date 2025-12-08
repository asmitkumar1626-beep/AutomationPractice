from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options (optional)
options = Options()
# Uncomment below to run headless (without opening a browser window)
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")

# Set up the Chrome driver using the Service object
service = Service(ChromeDriverManager().install())

# Create the driver
driver = webdriver.Chrome(service=service, options=options)

# Now you can use the driver
driver.get("https://www.google.com")
print(driver.title)

# Quit when done
driver.quit()
