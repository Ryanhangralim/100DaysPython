from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# price = driver.find_element(By.CLASS_NAME, value="menu")
# print({price.text})
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

driver.quit()