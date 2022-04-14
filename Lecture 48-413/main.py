from selenium import webdriver

chrome_driver_path = "/Users/nurayahmadova/SeleniumWebDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# goes to the url
# driver.get("https://www.amazon.com/Dyson-Airwrap-Styler-Shape/dp/B07MN2NBTT/ref=sr_1_2?crid=31WUTHPHMBG1J&dchild=1&"
#            "keywords=dyson+airwrap&qid=1630681313&sprefix=dyson+air+purifier+filter+replacements%2Caps%2C396&sr=8-2")
# price = driver.find_element_by_id("priceblock_ourprice").text
# print(price)

driver.get("https://www.python.org/")

search_bar = driver.find_element_by_name("q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element_by_xpath('/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# closes the tab
driver.close()

# quits the browser
driver.quit()