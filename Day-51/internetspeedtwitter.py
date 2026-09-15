from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self, url, password, email,down, up):
        self.url = url
        self.password = password
        self.email = email
        self.down = down
        self.up = up
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.maximize_window()
        check_speed = self.driver.find_element(By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button/h1')
        check_speed.click()
        download_speed = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3')))
        upload_speed = WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3')))

        if (float(upload_speed.text) < float(self.up)) or (float(download_speed.text) < float(self.down)):
            print("Tweeting about the internet complain.")
            message = f"Hey, Internet Provider, why is my internet speed {download_speed.text}down/ {upload_speed.text}up when I pay for {self.down}down/{self.up}up?"
            # self.driver.close()
            self.tweet_at_provider(message)

    def tweet_at_provider(self, message):
        self.driver.get(self.url)

        # 1. Fill in login fields
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))
        )
        login.send_keys(self.email)

        password_input = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password_input.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        # 2. Wait for the left navigation 'Post' button and click it to open the modal cleanly
        nav_post_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "compose")] | //button[contains(., "Post")]'))
        )
        self.driver.execute_script("arguments[0].click();", nav_post_btn)

        # 3. Wait for the modal box and type the message into the modal's input area
        modal_textbox = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="y-composer-modal"]//textarea | //*[@id="y-composer-modal"]//div[@role="textbox"]'))
        )
        modal_textbox.click()
        modal_textbox.send_keys(message)

        # 4. Click the "Post" button INSIDE the modal
        modal_submit_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="y-composer-modal"]//button[contains(., "Post")]'))
        )
        self.driver.execute_script("arguments[0].click();", modal_submit_btn)

        print("Tweet posted successfully!")





