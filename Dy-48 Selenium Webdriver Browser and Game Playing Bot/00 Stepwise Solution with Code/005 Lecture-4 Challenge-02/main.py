# 005 Challenge Use Selenium in a Blank Project & Scrape a Different Piece of Data



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)



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