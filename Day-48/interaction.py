# from html.entities import name

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://en.wikipedia.org/wiki/Main_Page'
x_path = '/html/body/div[2]/header/div[2]/div/div/div/div/form/div/div/div[1]'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get(url = url)
driver.maximize_window()

# element = driver.find_element(By.XPATH , value=x_path)
# print("".join(element.text.split(",")))
# element.click()

# you can also do this method by providing the actual item that has a link
# so the website has a item called gangrene which has another link when clicked so i will automatically
# click it by this method
# clicked = driver.find_element(By.LINK_TEXT, value = "gangrene")
# clicked.click()

#typing with the help of selenium
content = driver.find_element(By.CSS_SELECTOR, value="input.cdx-text-input__input")
content.send_keys("python")
content.send_keys(Keys.ENTER)





# driver.close()


