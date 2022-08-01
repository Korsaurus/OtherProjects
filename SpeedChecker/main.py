from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 15
chrome_driver_path = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
TWITTER_PASSWORD = "daw"
TWITTER_EMAIL = "wad"


class ISTwitterBot:

    def __init__(self, options, driver_path):
        self.driver = webdriver.Chrome(service=driver_path, options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        button.click()

        time.sleep(40)

        down_speed = int(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                        '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                        '2]/span').text)

        up_speed = int(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

        return down_speed, up_speed

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                   '1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                      '1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                           '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                           '1]/div/div/div/div[2]/div['
                                                           '1]/div/div/div/div/div/div/div/div/div/div['
                                                           '1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for" \
                f" {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                          '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                          '1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()


bot = ISTwitterBot(op, chrome_driver_path)

download_speed, upload_speed = bot.get_internet_speed()

if download_speed < PROMISED_DOWN or upload_speed < PROMISED_UP:
    bot.tweet_at_provider()
# could add a condition that checks if the location is correct and if not then say "VPN is on, doofus"

bot.driver.quit()
