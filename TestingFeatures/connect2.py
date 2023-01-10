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
    "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=23")
time.sleep(2)
# ----------------------------------------------------------------

all_connect_buttons = driver.find_elements(By.TAG_NAME, 'button')
connect_buttons = [
    btn for btn in all_connect_buttons if btn.text == "Connect"]

# handle folow buttons

all_names = []


all_span = driver.find_elements(
    By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")


idx = [*range(1, 11)]
for j in range(len(idx)):
    namme = all_span[j].text.split(" ")[0]
    all_names.append(namme)
    print(all_names)
    greetings = ["Hello", "Hi", "Dear"]




for i in range(0, len(connect_buttons)):

    


    driver.execute_script("arguments[0].click();", connect_buttons[i])
    time.sleep(2)
    custom_message_button = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]/span")

    time.sleep(2)
    driver.execute_script("arguments[0].click();", custom_message_button)

    greeting_idx = random.randint(0, len(greetings)-1)
    message = greetings[greeting_idx] + " " + \
        all_names[i] + \
        "! Let us connect. I hope we can benefit from each other in the future. Have a great day! "

    time.sleep(2)
    # print(message)
    #driver.execute_script("arguments[0].click();", custom_message_button)
    text_area = driver.find_element(By.XPATH, "//*[@id='custom-message']")

    time.sleep(2)

    text_area.send_keys(message)

    send = driver.find_element(
        By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span")
    if send:
        time.sleep(2)
        driver.execute_script("arguments[0].click();", send)
    else:
        close = driver.find_element(
            By.XPATH, "//button[@area-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)

    time.sleep(5)
