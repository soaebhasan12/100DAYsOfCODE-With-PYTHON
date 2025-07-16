# 002 How to Install & Set Up Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# chrome_driver_path = "C:/Development/chromedriver-win64/chromedriver.exe"
# service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com")

input("Press Enter to exit...")
driver.quit()