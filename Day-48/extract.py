from selenium import webdriver
from selenium.webdriver.common.by import By



url = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()#options=chrome_options
driver.get(url)

elements = driver.find_elements(By.XPATH, value='/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
for element in elements:
    upcoming_event_time = element.find_elements(By.TAG_NAME, value="time")
    upcoming_event = element.find_elements(By.TAG_NAME, value="a")

upcoming_event_list = [upcoming_event.text for upcoming_event in upcoming_event]
upcoming_event_time_list = [upcoming_event.text for upcoming_event in upcoming_event_time]
print(upcoming_event_list)
print(upcoming_event_time_list)
event_dic = {}
# event_dic[0] = "dina"
print(event_dic)
for i in range(len(upcoming_event_time_list)):
    event_dic[i] = {"time": upcoming_event_time_list[i],
                    "name": upcoming_event_list[i]}
print(event_dic)








driver.close()