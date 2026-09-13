from selenium import webdriver
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
URL = os.environ['URL']

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Set path and add profile argument
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()


login_button = driver.find_element(By.ID, value="login-button")
login_button.click()
email_input = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div/form/div[1]/input')))
# email_input = driver.find_element(By.XPATH, value='/html/body/div/main/div/form/div[1]/input')
email_input.send_keys(EMAIL)

password_input = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div/form/div[2]/input')))
# password_input = driver.find_element(By.XPATH, value='/html/body/div/main/div/form/div[2]/input')
password_input.send_keys(PASSWORD)


submit_button = driver.find_element(By.XPATH,value = '/html/body/div/main/div/form/button')
submit_button.click()

booked_date = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div/div[4]/h2')))
book_button =  WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/main/div/div[4]/div[5]/div/div[2]/button')))
if book_button.text == 'Book Class':
    book_button.click()
    print(f"Booked spin class for {booked_date.text} at 6:00 pm")




