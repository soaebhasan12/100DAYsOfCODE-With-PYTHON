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
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR_REGISTERED_GMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        self.driver = driver
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
    
    def get_internet_speed(self):
        self.driver = driver.get("https://www.speedtest.net/")
        sleep(10)
        driver.maximize_window()

        self.go_button = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a").click()
        
        sleep(60)
        self.download_speed = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        print(f"Download Speed: {self.download_speed}")

        self.upload_speed = driver.find_element(By.XPATH, "//*[@id='container']/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(f"Download Speed: {self.upload_speed}")


    
    def tweet_at_provider(self):
        print("This method will tweet at the internet provider.")

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)

bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()
bot.tweet_at_provider()

