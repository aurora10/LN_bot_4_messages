from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

# /Users/rob/Downloads/chromedriver
# LOGIN
driver = webdriver.Chrome('/Users/rob/Downloads/chromedriver')
driver.get('https://www.linkedin.com/')

time.sleep(2)
username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')

username.send_keys("zimrob1010@gmail.com")
password.send_keys("3iver5rr6pta393htful2int7ons")
time.sleep(2)

submit = driver.find_element(
    By.XPATH, "/html/body/main/section[1]/div/div/form/button")
driver.execute_script("arguments[0].click()", submit)
time.sleep(2)

# link to people you need to message
# https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&sid=ZE(

n_pages = 1

for n in range(0, n_pages):

    driver.get(
        "" + str(n))
        # https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aautocomplete%3A-207530251&keywords=trucking%20company&network=%5B%22F%22%5D&origin=FACETED_SEARCH&position=0&searchId=ca1bb25f-d29b-4b9e-916f-69dc21c7d841&sid=e9.
    time.sleep(2)

# Clicking on Message button

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(0, len(message_buttons)):  # (0, len(message_buttons)) when in production

        driver.execute_script("arguments[0].click()", message_buttons[i])
        time.sleep(3)

        # ACTIVATE THE MAIN DIV ON MESSAGE FORM

        main_div = driver.find_element(
            By.XPATH, "//div[starts-with(@class,'msg-form__msg-content-container')]")
        driver.execute_script("arguments[0].click()", main_div)

        time.sleep(3)


# FIND P TAG AND SEND KEYS
        paragraphs = driver.find_elements(By.TAG_NAME, "p")

        # FIND CORRECT P TAG

        # counter = 0
        # for p in paragraphs:
        #     print(counter)
        #     print(p.text)
        #     counter += 1
        # print(paragraphs[-5].text)

# FIND SPANS CONTAINING FULLNAME
        all_span = driver.find_elements(
            By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")

        idx = [*range(1, 11)]
        greetings = ["Hello", "Hi", "Dear"]
        all_names = []

        for j in range(len(idx)):
            namme = all_span[j].text.split(" ")[0]
            all_names.append(namme)

        greeting_idx = random.randint(0, len(greetings)-1)
        message = greetings[greeting_idx] + " " + \
            all_names[i] + "! Thank you for accepting my connection request! Just wanted to let you know that I am looking to acquire a transport company in your area and if happen to know someone who in looking for an exit, would you let me know? Regards. Rob "

        paragraphs[-5].send_keys(message)
        time.sleep(2)

# PRESS SUBMIT BUTTON
        submit = driver.find_element(By.XPATH, "//button[@type='submit']")
        driver.execute_script("arguments[0].click()", submit)
        time.sleep(4)

# LOCATE CLOSE_BUTTON
        close_button = driver.find_element(
            By.XPATH, "//button[starts-with(@class,'msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1')]")
        driver.execute_script("arguments[0].click()", close_button)
        time.sleep(3)
