import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time  

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=option
)


FORM_URL = "https://forms.gle/JNWqD9vhHyQdC9PT7"  # Replace with your Google Form URL


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
# time.sleep(17) # Wait for the user to log in to the browser
driver.maximize_window()
zillow_web = driver.get(zillow_clone_url)
response = requests.get(zillow_clone_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings:\n")
print(all_links)

all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
print(f"\n{len(all_addresses)} cleaned addresses:\n")
print(all_addresses)

all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]
print(f"\n{len(all_prices)} cleaned prices:\n")
print(all_prices)


time.sleep(11)
driver.maximize_window()

for n in range(len(all_links)):
    driver.get(FORM_URL)
    time.sleep(2)

    address = driver.find_element(By.XPATH, 
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, 
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, 
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, 
                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    time.sleep(1)
    address.send_keys(all_addresses[n])
    time.sleep(1)
    price.send_keys(all_prices[n])
    time.sleep(1)
    link.send_keys(all_links[n])
    time.sleep(1)
    submit_button.click()
    time.sleep(1)

driver.quit()