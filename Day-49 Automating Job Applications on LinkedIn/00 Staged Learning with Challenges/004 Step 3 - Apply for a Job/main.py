import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)



job_application_url = "https://www.linkedin.com/jobs/search-results/?currentJobId=4263967231&eBP=NON_CHARGEABLE_CHANNEL&f_AL=true&keywords=Intern&refId=OIu5HJLi%2FwLJ6mXWBbNjqw%3D%3D&trackingId=x6CifTd7zlQpDjU%2FsuqnJQ%3D%3D"

driver.get(job_application_url)


time.sleep(5)

load_dotenv(dotenv_path="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/Day-49 Automating Job Applications on LinkedIn/Day-49 Automating Job Applications on LinkedIn/00 Staged Learning with Challenges/credit.env", override=True)




ACCOUNT_EMAIL = os.getenv("USERNAME")
ACCOUNT_PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("CONTACT")




username = driver.find_element(By.NAME, "session_key")
username.click()
username.send_keys(os.getenv("USERNAME"))
password = driver.find_element(By.NAME, "session_password")
password.click()
password.send_keys(os.getenv("PASSWORD"))
SignIn = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
SignIn.click()

#Locate the apply button
time.sleep(30)
apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
apply_button.click()


#Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()