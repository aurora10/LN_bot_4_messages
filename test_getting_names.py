import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# /Users/rob/Downloads/chromedriver
# LOGIN
driver = webdriver.Chrome('/Users/rob/Downloads/chromedriver')
driver.get('https://www.linkedin.com/')

time.sleep(2)
username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')

username.send_keys("hello@marketorix.com")
password.send_keys("zbbc6tEurgdSGhQ")
time.sleep(2)

submit = driver.find_element(
    By.XPATH, "/html/body/main/section[1]/div/div/form/button")
driver.execute_script("arguments[0].click()", submit)
time.sleep(2)

driver.get(
    "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=ZE(")

time.sleep(2)

all_span = driver.find_elements(
    By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")

counter = 1
for i in all_span:
    print(counter)
    print(i.text)
    counter += 1

idx = [*range(1, 11)]
greetings = ["Hello", "Hi", "Dear"]

print(idx)

for i in range(len(idx)):
    greeting_idx = random.randint(0, len(greetings)-1)
    namme = all_span[i].text.split(" ")[0]
    print(greetings[greeting_idx] + " " + namme + ", nice to meet you! ")
