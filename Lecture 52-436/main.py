import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

FIREFOX_DRIVER_PATH = "/Users/nurayahmadova/SeleniumWebDriver/geckodriver"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "python_test_123"
PASSWORD = "PYTHON123"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Firefox(executable_path=driver_path)
        self.driver.fullscreen_window()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main''/div/div/div/div/button').click()
        # time.sleep(10)
        # self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/span')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element
            # by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(FIREFOX_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
