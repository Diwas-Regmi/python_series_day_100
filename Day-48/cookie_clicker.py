
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set initial timers
five_sec_check = time.time() + 15
timeout = time.time() + 5*60  # 5-minute game run time

url = 'https://ozh.github.io/cookieclicker/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url = url)
driver.maximize_window()

time.sleep(2)
english_select = driver.find_element(By.ID, value="langSelect-EN")
english_select.click()

# cookie button
cookie_button = driver.find_element(By.ID, value="bigCookie")

# # Running the program now


time.sleep(2)
clicked = True
time.sleep(2)
while True:
    cookie_button = driver.find_element(By.ID, value="bigCookie")
    cookie_button.click()
    if time.time() > five_sec_check:
        items_clickable = driver.find_elements(By.CSS_SELECTOR, value='.product.unlocked.enabled')
        if items_clickable:
            driver.execute_script("arguments[0].click();", items_clickable[-1])

        # Safely attempt to click each close button and ignore stale element errors
        close_buttons = driver.find_elements(By.CSS_SELECTOR, value='#notes .close')
        for button in close_buttons:
            try:
                driver.execute_script("arguments[0].click();", button)
            except Exception:
                pass  # Ignore stale element if the DOM refreshed mid-loop
        # Reset the 1-second timer
        five_sec_check = time.time() + 5


    if time.time() > timeout:
        break
cookie_per_second = driver.find_element(By.CSS_SELECTOR, value='#cookiesPerSecond')
print(f"Cookies_Per_Second : {cookie_per_second.text.split(":")[1].strip()}")






# driver.close()
