from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.XPATH, value="//*[@id='articlecount']/a[1]")
print(count.text)

#2nd solution
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

driver.quit()