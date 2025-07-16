import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



options  = Options()
options.add_experimental_option("detach", True)


driver1 = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver1.get("https://en.wikipedia.org/wiki/Main_Page")


# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# print(article_count.text)
article_count1 = driver1.find_element(By.CSS_SELECTOR, "#articlecount > ul > li:nth-child(2) > a:nth-child(1)")
# print(article_count1.text)







# 06 : How to Automate Filling Out Forms and Clicking buttons with Selenium.

all_portals = driver1.find_element(By.LINK_TEXT, "Reference desk")
# all_portals.click()


# Resize window
driver1.set_window_size(1200, 800)


time.sleep(2)
search = driver1.find_element(By.NAME, "search")
search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)        # to see more keys visit Keys.py (Click on 'Keys')





# Challenge: Practice using Selenium fill in this form and clicking Sign up.

time.sleep(10)


form_page_url = "http://secure-retreat-92358.herokuapp.com/"

driver2 = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver2.get(form_page_url)

first_name = driver2.find_element(By.NAME, "fName")
first_name.click()
first_name.send_keys("Soaeb")

last_name = driver2.find_element(By.NAME, "lName")
last_name.click()
last_name.send_keys("Hasan")

email_addrs = driver2.find_element(By.NAME, "email")
email_addrs.click()
email_addrs.send_keys("saibuhasan22@gmail.com")


submit = driver2.find_element(By.CSS_SELECTOR, "form button")
submit.send_keys(Keys.ENTER)
# submit.click()