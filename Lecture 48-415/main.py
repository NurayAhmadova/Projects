from selenium import webdriver

chrome_driver_path = "/Users/nurayahmadova/SeleniumWebDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]").text
print(article_count)


driver.close()
driver.quit()
