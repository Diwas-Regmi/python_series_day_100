from selenium import webdriver
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

email_input = driver.find_element(By.XPATH, value='/html/body/div/main/div/form/div[1]/input')
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.XPATH, value='/html/body/div/main/div/form/div[2]/input')
password_input.send_keys(PASSWORD)

submit_button = driver.find_element(By.XPATH,value = '/html/body/div/main/div/form/button')
submit_button.click()

class_schedule = driver.find_elements(By.XPATH, value="/html/body/div/main/div")
for classes in c    

# # Wait up to 10 seconds for the element to load
# wait = WebDriverWait(driver, 10)
# booked_date = wait.until(
#     EC.presence_of_element_located((By.ID, "day-title-tue,-sep-15"))
# )
# print(booked_date.text)
#



# driver.close()
