from selenium import webdriver
from selenium.webdriver.common import driver_finder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
URL = os.environ["URL"]



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#
# # Set path and add profile argument
# user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# chrome_options.add_argument(f"--user-data-dir={user_data_dir}")



driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()


login_button = driver.find_element(By.XPATH, value = "/html/body/header/button")
login_button.click()

facebook_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')))
facebook_button.click()

# ----------------------------------------------------
# NEW STEP: Switch to the Facebook Pop-up Window
# ----------------------------------------------------
time.sleep(2)  # Give the popup a moment to open
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# 3. Fill in email and password in the popup window
email_fillup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))  # Using name locator is more reliable than absolute XPath
)
email_fillup.send_keys(EMAIL)

password_fillup = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "pass"))
)
password_fillup.send_keys(PASSWORD)

fb_login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
fb_login_btn.click()

# 5. Switch driver back to the main window (popup automatically closes after submit)
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 1)
driver.switch_to.window(base_window)

# 6. Click location / notification allow prompt on main page
allow_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Allow')]"))
)
allow_button.click()


# 7. Step 2 Modal: Wait for location modal to disappear, THEN locate and click "Enable"
WebDriverWait(driver, 10).until(EC.staleness_of(allow_button))

enable_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/main/div/div/form/button[1]")
    )
)
enable_button.click()

# 8. Step 3 Modal: Wait for enable modal to disappear, THEN locate and click "I accept"
WebDriverWait(driver, 10).until(EC.staleness_of(enable_button))

accept_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/form/button"))
)
accept_button.click()
# Replace Step 9 with this complete loop:

while True:
    try:
        # 1. Check if we ran out of profiles
        no_more_dogs = driver.find_elements(
            By.XPATH, "//*[contains(text(), 'No more dogs in your area')]"
        )
        if no_more_dogs:
            print("Finished swiping: No more dogs in your area!")
            break

        # 2. Check if a match popup appeared
        match_popup = driver.find_elements(
            By.XPATH,
            "//a[contains(text(),'Back to Tindog')] | //button[contains(text(),'Back to Tindog')]",
        )
        if match_popup:
            match_popup[0].click()
            print("Dismissed match popup!")
            time.sleep(1)

        # 3. Click the Like button via JS
        like_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="like-button-container"]/form/button')
            )
        )
        driver.execute_script("arguments[0].click();", like_button)
        print("Liked a profile!")
        time.sleep(1)

    except Exception:
        # Small wait if elements are mid-transition
        time.sleep(1)