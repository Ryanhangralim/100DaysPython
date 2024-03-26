from selenium import webdriver
from selenium.webdriver.common.by import By

# Keeps chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.tokopedia.com/grosirgamebec/game-nintendo-switch-persona-5-royal?extParam=ivf%3Dfalse%26src%3Dsearch")

price = driver.find_element(By.CLASS_NAME, value="price")
print({price.text})

driver.quit()