from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


PROMISED_DOWN = 150
PROMISED_UP = 50
TWITTER_EMAIL = "YOUR_REGISTERED_GMAIL"
TWITTER_USERNAME = "YOUR_TWITTER_USERNAME"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.driver = driver
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
    
    def get_internet_speed(self):
        self.driver = driver.get("https://www.speedtest.net/")
        sleep(5)
        driver.maximize_window()

        go_button = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a").click()
        
        sleep(40)
        download_speed = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        print(f"Download Speed: {download_speed}")

        upload_speed = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(f"Download Speed: {upload_speed}")


    
    def tweet_at_provider(self):
        self.driver = driver.get("https://x.com/login")
        sleep(5)
        driver.maximize_window()


        input_email = driver.find_element(By.NAME, 'text')
        input_email.send_keys(TWITTER_EMAIL)
        sleep(2)
        input_email.send_keys(Keys.ENTER)


        # next_button = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div").click()
        # sleep(2)

        username = driver.find_element(By.NAME, "text")
        username.send_keys(TWITTER_USERNAME)
        sleep(2)
        username.send_keys(Keys.ENTER)
        sleep(2)

        next_button = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div").click()
        sleep(2)

        password = driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        post = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div").click()
        sleep(2)
        post.send_keys(f"Hey Internet Provider, why is my internet speed {self.download_speed} down/{self.upload_speed} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up? Fix your service!")
        sleep(2)

        tweet_button = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button").click()



options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)

bot = InternetSpeedTwitterBot(driver)
# bot.get_internet_speed()
bot.tweet_at_provider()