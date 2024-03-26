from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

price = driver.find_element(By.XPATH, value="//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[2]")
date, name = price.text.split("\n")
print(f"{date} /// {name}")

upcoming_events = {}

for i in range(5):
    event = driver.find_element(By.XPATH, value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i+1}]")
    date, name = event.text.split("\n")
    event_info = {"time": date, "name": name}
    upcoming_events[i] = event_info

print(upcoming_events)

#2nd solution
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

upcoming_events2 = {}

for n in range(len(event_times)):
    upcoming_events2[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(upcoming_events2)

driver.quit()