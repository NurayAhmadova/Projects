from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
FIREFOX_DRIVER_PATH = "/Users/nurayahmadova/SeleniumWebDriver/geckodriver"
TWITTER_EMAIL = "python.test.n.a@gmail.com"
TWITTER_PASSWORD = "PYTHON123"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        # self.firefox_driver_path = "/Users/nurayahmadova/SeleniumWebDriver/geckodriver"
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.driver.fullscreen_window()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')

        time.sleep(3)
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element_by_class_name("upload-speed").text
        print(f"upload: {self.up}")

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        time.sleep(10)
        name = self.driver.find_element_by_name("session[username_or_email]")
        name.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span")
        tweet.click()
        tweet_compose = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)

        tweet_button = self.driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span")

        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(FIREFOX_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
