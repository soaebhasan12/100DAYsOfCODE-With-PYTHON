# 004 Challenge Use Selenium to Scrape Website Data


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)


# Challenge: Extract the upcoming event from the python.org website. use selenium to scrape all upcoming event dates and event names (in my case there are 5) and store them in a nested dictionary. Print the dictionary to the console. the event data from python.org should be stored under the keys "time" and "name"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org/")

event_time_elements = driver.find_elements(By.CSS_SELECTOR, ".event-widget > .shrubbery > ul > li > time")
event_name_elements = driver.find_elements(By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a")


# for time in event_time_elements:
#     print(time.text)

# for name in event_name_elements:
#     print(name.text)

events_dict = {}


for i in range(len(event_time_elements)):
    full_date = event_time_elements[i].get_attribute("datetime").split("T")[0]
    event_name = event_name_elements[i].text

    # Store in dictionary using index as key
    events_dict[i] = {
        "time": full_date,
        "name": event_name
    }


print(events_dict)

input("Press Enter to exit...")
driver.quit()