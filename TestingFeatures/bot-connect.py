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

username.send_keys("hello@marketorix.com")
password.send_keys("zbbc6tEurgdSGhQ")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(2)

n_pages = 3

for n in range(1, n_pages):

    driver.get(
        "https://www.linkedin.com/search/results/people/?keywords=founder%20or%20owner%20&origin=GLOBAL_SEARCH_HEADER&page="
        + str(n))
    time.sleep(2)

    all_names = []

    all_connect_buttons = driver.find_elements(By.TAG_NAME, 'button')
    message_buttons = [
        btn for btn in all_connect_buttons if btn.text == "Connect"]
    all_span = driver.find_elements(
        By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")
    for i in range(0, len(message_buttons)):
        idx = [*range(1, 11)]
        for j in range(len(idx)):
            namme = all_span[j].text.split(" ")[0]
            all_names.append(namme)
            print(all_names)
            greetings = ["Hello", "Hi", "Dear"]

            greeting_idx = random.randint(0, len(greetings)-1)
            message = greetings[greeting_idx] + " " + \
                all_names[i] + \
                "! I hope I can bring some value to your network. Have a great day! "

            message = " Hi " + \
                all_names[i] + \
                "! I hope I can bring some value to your network. Have a great day! "

        driver.execute_script("arguments[0].click();", message_buttons[i])

        all_buttons1 = driver.find_elements(
            By.TAG_NAME, 'button')  # Do we need this?

        custom_message_button = driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]/span")

        time.sleep(2)

        driver.execute_script("arguments[0].click();", custom_message_button)

        time.sleep(2)

        message = driver.find_element(By.ID, "custom-message")

        message.send_keys(message)
        time.sleep(2)

        # send = driver.find_element(
        #     By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]/span")

        # driver.execute_script("arguments[0].click();", send)

        time.sleep(2)
