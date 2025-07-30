# 003 How to Find and Select Elements on a Website with Selenium


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# chrome_driver_path = "C:/Development/chromedriver-win64/chromedriver.exe"
# service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-price-whole")
print(price.text)

input("Press Enter to exit...")
driver.quit()