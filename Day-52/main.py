import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


load_dotenv()
URL = os.environ['URL']
PASSWORD = os.environ['PASSWORD']
EMAIL = os.environ['EMAIL']
TARGET = os.environ['TARGET']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, value = '/html/body/div/aside/div/form/input[1]')
user_name.send_keys(EMAIL)

password = driver.find_element(By.XPATH, value = '/html/body/div/aside/div/form/input[2]')
password.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH, value = '/html/body/div/aside/div/form/button')
login_button.click()

not_now_button = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]')))
not_now_button.click()
not_now_button = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[4]/div/button[2]')))
not_now_button.click()

search_button = driver.find_element(By.XPATH, value = '/html/body/div[1]/nav/button')
search_button.click()

search_target = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'/html/body/aside/div[4]/a[1]')))
search_target.click()

followers = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')))
followers.click()

## --- FIXED FOLLOW & SCROLL LOOP ---

# 1. Target the scrollable modal container
modal_container = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]'))
)

# 2. Set how many scroll attempts you want to perform
scrolls = 5

for i in range(scrolls):
    # Find all currently loaded follow buttons
    buttons = modal_container.find_elements(By.XPATH, './/button[contains(@class, "naan-follow-btn")]')
    print(f"Batch {i+1}: Found {len(buttons)} total buttons loaded so far.")

    # Iterate and click un-followed buttons
    for button in buttons:
        is_following = button.get_attribute("data-following")
        if is_following == "false":
            driver.execute_script("arguments[0].click();", button)
            time.sleep(1) # Delay between clicks to avoid action blocks

    # Scroll down to the bottom of the modal container to trigger lazy loading
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal_container)
    time.sleep(2) # Wait for new accounts to load into the HTML