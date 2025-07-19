import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)



job_application_url = "https://www.linkedin.com/jobs/search-results/?distance=50&f_AL=true&geoId=106893311&keywords=Python%20Developer&origin=JOBS_HOME_SEARCH_BUTTON"

driver.get(job_application_url)


time.sleep(5)

load_dotenv(dotenv_path="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/Day-49 Automating Job Applications on LinkedIn/Day-49 Automating Job Applications on LinkedIn/00 Staged Learning with Challenges/credit.env", override=True)

username = driver.find_element(By.NAME, "session_key")
username.click()
username.send_keys(os.getenv("USERNAME"))


password = driver.find_element(By.NAME, "session_password")
password.click()
password.send_keys(os.getenv("PASSWORD"))

print(username)
print(password)

SignIn = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
SignIn.click()