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

username.send_keys("robert@marketorix.com")
password.send_keys("w2vGWGqJNEc2iCTBkH8SaGZ")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(4)


driver.get(
    "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=20")
time.sleep(3)

################################################################ connection

time.sleep(3)
all_buttons = [button.text for button in driver.find_elements(By.TAG_NAME, 'button') if button.text == "Connect" or button.text == "Follow" or button.text == "Pending"]
time.sleep(3)

##########################Get All Possible Buttons
all_connect_buttons = driver.find_elements(By.TAG_NAME, 'button')
connect_buttons = [
    btn for btn in all_connect_buttons if btn.text == "Connect"]
####### ########### ########### ########### ########### ########### ########### get all Connect Buttons

all_span_names = driver.find_elements(
    By.XPATH, "//a[contains(@class,'app-aware-link ')]/span[@dir='ltr']/span[@aria-hidden='true']")

######################### Get all spans that have Names      

time.sleep(3) 

all_names = []

idx = [*range(1, 11)]
for j in range(len(idx)):
    namme = all_span_names[j].text.split(" ")[0]
    all_names.append(namme)
    print(all_names)
greetings = ["Hello", "Hi", "Dear"]

######################## Index Name positions and get first_name -> append to all_names
        
size = len(all_buttons)
names_to_be_conneceted = []
for i in range(size):
    if all_buttons[i] == "Connect":
            names_to_be_conneceted.append( all_names[i]) 
print(names_to_be_conneceted)
################################################################ Filter only names that have Connect Button (not Follow or Pending)
for i in range(0, len(connect_buttons)):

        time.sleep(3)
        driver.execute_script("arguments[0].click();", connect_buttons[i])
        time.sleep(2)
        ########################    click on connect_buttons
        custom_message_button = driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]/span")


        time.sleep(2)
        driver.execute_script("arguments[0].click();", custom_message_button)

        ######################### find custom_message_button and click

        greeting_idx = random.randint(0, len(greetings)-1)
        message = greetings[greeting_idx] + " " +names_to_be_conneceted[i] + \
                    "! Let us connect. I hope we can benefit from each other in the future. Have a great day! "

        time.sleep(2)
        ######################## get random greeting from greetings array and compose a message
        text_area = driver.find_element(By.XPATH, "//*[@id='custom-message']")

        time.sleep(2)

        text_area.send_keys(message)

        ################### select text_area and insert message

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




