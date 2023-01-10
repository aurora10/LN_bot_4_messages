from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from pprint import pprint
import time
import random


driver = webdriver.Chrome("/Users/rob/Downloads/chromedriver", chrome_options=chrome_options)
driver.get("https://www.linkedin.com/")

time.sleep(2)

username = driver.find_element("xpath", "//input[@name='session_key']")
password = driver.find_element("xpath", "//input[@name='session_password']")

username.send_keys("hello@marketorix.com")
password.send_keys("zbbc6tEurgdSGhQ")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(2)


driver.get(
    "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=4")
time.sleep(3)

all_span_names = driver.find_elements(
    By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")

time.sleep(3)
all_buttons = [button.text for button in driver.find_elements(By.TAG_NAME, 'button') if button.text == "Connect" or button.text == "Follow"]
time.sleep(3)





all_names = []



idx = [*range(1, 11)]
for j in range(len(idx)):
    namme = all_span_names[j].text.split(" ")[0]
    all_names.append(namme)
    print(all_names)
     
        
size = len(all_buttons)
res = []
for i in range(size):
    if all_buttons[i] == "Connect":
        res.append( (all_names[i]) )
print(res)




