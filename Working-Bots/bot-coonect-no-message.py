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

n_pages = 1
# https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=7
# for n in range(0, n_pages):

        # driver.get(
        #     "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106204383%22%5D&heroEntityKey=urn%3Ali%3Aautocomplete%3A402508361&keywords=it%20recruiter&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=" + str(n))
        # time.sleep(2)

driver.get(
            "https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106204383%22%5D&heroEntityKey=urn%3Ali%3Aautocomplete%3A402508361&keywords=it%20recruiter&network=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page=3")
        # ----------------------------------------------------------------

all_connect_buttons = driver.find_elements(By.TAG_NAME, 'button')
connect_buttons = [
btn for btn in all_connect_buttons if btn.text == "Connect"]
for i in range(0, len(connect_buttons)):
    driver.execute_script("arguments[0].click();", connect_buttons[i])
    time.sleep(3)
    
#   try to send connection if send button is apearing
    
    try:
        send = driver.find_element(
                By.XPATH, "//button[@aria-label='Send now']")
        time.sleep(3)        
        driver.execute_script("arguments[0].click();", send)
        time.sleep(3)
    except:    
# else anser: how do you know this person? and press other and connect button               
        time.sleep(3)
        other = driver.find_element(
                        By.XPATH, "//button[@aria-label='Other']")
        driver.execute_script("arguments[0].click();", other)
        time.sleep(3)
        connect = driver.find_element(By.XPATH, "//button[@aria-label='Connect']")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", connect)
                
            
            
