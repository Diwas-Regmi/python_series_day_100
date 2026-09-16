import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


class FillForm:
    def __init__(self, url, price_list, address_lists, links_to_appartment):
        self.url = url
        self.price = price_list
        self.address = address_lists
        self.link = links_to_appartment
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)

    def form_fill_up(self):
        driver = webdriver.Chrome(options=self.chrome_options)
        driver.maximize_window()

        for i in range(len(self.address)):
            # Freshly load the form for each submission
            driver.get(self.url)

            # 1. Wait until input fields exist
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//input[@type="text" or @type="url"]'))
            )

            inputs = driver.find_elements(By.XPATH, '//input[@type="text" or @type="url"]')

            inputs[0].send_keys(self.address[i])
            inputs[1].send_keys(self.price[i])
            inputs[2].send_keys(self.link[i])

            # 2. Click the Submit button
            submit_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//div[@role="button" and @aria-label] | //div[@role="button"]//span'))
            )
            submit_btn.click()

            # 3. Sleep briefly to guarantee submission request goes through before re-navigating
            time.sleep(1)

        driver.quit()