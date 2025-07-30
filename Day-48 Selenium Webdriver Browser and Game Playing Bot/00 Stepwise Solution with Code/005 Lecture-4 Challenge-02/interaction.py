from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Challenge: Create a blank file called interaction.py. Use selenium to print the total number of articles from the wikipedia homepage to the console.


options  = Options()
options.add_experimental_option("detach", True)


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(article_count.text)
article_count1 = driver.find_element(By.CSS_SELECTOR, "#articlecount > ul > li:nth-child(2) > a:nth-child(1)")
print(article_count1.text)