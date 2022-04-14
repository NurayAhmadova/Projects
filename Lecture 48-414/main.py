from selenium import webdriver

chrome_driver_path = "/Users/nurayahmadova/SeleniumWebDriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

event_dates = driver.find_elements_by_css_selector('.event-widget time')

event_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {}

for n in range(len(event_dates)):
    events[n] = {
        "time": event_dates[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.close()
driver.quit()
