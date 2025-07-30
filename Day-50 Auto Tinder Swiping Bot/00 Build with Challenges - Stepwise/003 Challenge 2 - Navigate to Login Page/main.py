from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


tinder_url = "https://tinder.com/"

options = Options()
options.add_experimental_option("detach", True)

# Use ChromeDriverManager to get the cached path
driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)


driver.get(tinder_url)

driver.maximize_window()
sleep(3)

# Example: Accept cookies or consent screen
try:
    consent_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[.//div[text()="I accept"]]'))
    )
    consent_btn.click()
    sleep(2)  # Wait for UI to update
except Exception as e:
    print("Consent button not found or not clickable.", e)


login = driver.find_element(By.LINK_TEXT, value='Log in')
sleep(2)
login.click()


sleep(4)
more_options = driver.find_element(By.CSS_SELECTOR, "#o787701392 > div > div > div > div > div > div > div > div > span > button")
more_options.click()


sleep(4)
login_facebook = driver.find_element(By.XPATH, value = '//*[@id="o787701392"]/div/div/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div')
login_facebook.click()