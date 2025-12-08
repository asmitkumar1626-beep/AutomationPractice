from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demoqa.com/menu")

# Click "Sub Sub Item 2" directly via JS
driver.execute_script("""
document.querySelectorAll('a').forEach(el => {
    if(el.textContent.trim() === 'Sub Sub Item 2'){
        el.click();
    }
});
""")
print("Clicked Sub Sub Item 2 via JS")
driver.quit()



