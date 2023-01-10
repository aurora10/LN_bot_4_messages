from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

driver = webdriver.Chrome("/Users/rob/Downloads/chromedriver")
driver.get("https://www.linkedin.com/")

time.sleep(2)

username = driver.find_element("xpath", "//input[@name='session_key']")
password = driver.find_element("xpath", "//input[@name='session_password']")

username.send_keys("robert@marketorix.com")
password.send_keys("w2vGWGqJNEc2iCTBkH8SaGZ")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(2)

driver.get(
    "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=2")
time.sleep(2)
# ----------------------------------------------------------------

# all_connect_buttons = driver.find_elements(By.TAG_NAME, 'button')
# connect_buttons = [
#     btn for btn in all_connect_buttons if btn.text == "Connect"]

# handle folow buttons
#follow_buttons = [btn for btn in all_connect_buttons if btn.text == "Follow"]
all_connect_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label,'Invite')]")


all_names = []
all_span = driver.find_elements(
    By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")

    

for i in range(len(all_connect_buttons)):
    name = all_span[i].text
    all_names.append(name) 

    print(all_names)

# idx = [*range(1, 11)]
# for j in range(len(idx)):
    
#     namme = all_span[j].text.split(" ")[0]
#     all_names.append(namme)

#     print(namme)
    
# <span class="artdeco-button__text">
#     Connect
# </span>

# <span class="artdeco-button__text">
#     Follow
# </span>