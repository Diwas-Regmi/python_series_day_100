from pydoc import cli

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://ozh.github.io/cookieclicker/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url = url)
driver.maximize_window()

time.sleep(2)
english_select = driver.find_element(By.ID, value="langSelect-EN")
english_select.click()
i = 1
clicked = True
time.sleep(2)
while clicked:

    cookie_button = driver.find_element(By.ID, value="bigCookie")
    cookie_button.click()
    # i +=1
    # if i>100:
    #     clicked = False













# driver.close()
