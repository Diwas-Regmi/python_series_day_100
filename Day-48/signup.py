from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://appbrewery.github.io/fake-newsletter-signup/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(url = url)
driver.maximize_window()
first_name = driver.find_element(By.NAME, value="fName")
last_name =  driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
# username = driver.find_element(By.CLASS_NAME, value="btn-primary")
# username = driver.find_element(By.CSS_SELECTOR, value="button.btn btn-lg btn-primary btn-block")
username = driver.find_element(By.TAG_NAME, value="button")

first_name.send_keys("Diwas")
last_name.send_keys("Regmi")
email.send_keys("diwas@gmail.com")
username.click()




# driver.close()
