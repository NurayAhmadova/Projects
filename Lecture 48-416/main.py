from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/nurayahmadova/SeleniumWebDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# # article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
FIRSTNAME = "Nuray"
LASTNAME = "Ahmadova"
EMAIL = "nuray.akhmedova@gmail.com"

fname = driver.find_element_by_name("fName")
fname.send_keys(FIRSTNAME)
fname.send_keys(Keys.ENTER)

lname = driver.find_element_by_name("lName")
lname.send_keys(LASTNAME)
lname.send_keys(Keys.ENTER)

email = driver.find_element_by_name("email")
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)

sign_up = driver.find_element_by_link_text("submit").click()

driver.close()
driver.quit()
