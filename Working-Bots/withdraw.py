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

username.send_keys("zimrob1010@gmail.com")
password.send_keys("3iver5rr6pta393htful2int7ons")
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']")
driver.execute_script('arguments[0].click();', submit)
time.sleep(2)


driver.get(
    "https://www.linkedin.com/mynetwork/invitation-manager/sent/")


withdraw_buttons = [button for button in driver.find_elements(By.TAG_NAME, 'button') if button.text == "Withdraw"]


time.sleep(3)
for i in range(0, len(withdraw_buttons)):
    # expiry condition logic here   
    
    driver.execute_script('arguments[0].click();', withdraw_buttons[i])
    time.sleep(2)
    withdraw = driver.find_element("xpath", "/html/body/div[3]/div/div/div[3]/button[2]/span")
    driver.execute_script('arguments[0].click();', withdraw)
    time.sleep(2)