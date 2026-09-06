from selenium import webdriver
from selenium.webdriver.common.by import By
#keep the chrome open

url = "https://www.flipkart.com/emporio-armani-analog-watch-men/p/itmbfd665b7954b3?pid=WATHE49PFZSSRNZX&lid=LSTWATHE49PFZSSRNZXMKBQFC&marketplace=FLIPKART&q=watch&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=en_DIOVXIpLl34LEJ77ZDdFrTbDPYKco3y7fWovYOyD0zpPgRXfw2k-O43Bu1bktHL279FfU0iSFfjFxd7H0-o_qdG87K3oCe50S9wUJGhgG8IoL-c34-Tn23Ru0Z6W5Vp7&ppt=dynamic&ppn=Login%3ACategory_List&ssid=4jahpioa4g0000001788685802279&qH=d2974c96dc96b3f3&ov_redirect=true"
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)
driver.get(url= url)
# <div class= style="display: flex; flex-basis: auto; flex-direction: column; flex-shrink: 0; align-items: stretch; min-height: 0px; min-width: 0px; position: relative; z-index: 0; box-sizing: border-box; border-width: 0px;"><a class="_1psv1zeb9 _1o6mltlk4" style="align-items: stretch; box-sizing: border-box; display: flex; flex-basis: auto; flex-direction: column; flex-shrink: 0; min-height: 0px; min-width: 0px; position: relative; z-index: 0; border-width: 0px;"><div class="_1psv1zeb9 _1psv1ze0" style="display: flex; flex-basis: auto; flex-direction: row; flex-shrink: 0; align-items: center; min-height: 0px; min-width: 0px; position: relative; z-index: 0; box-sizing: border-box; border-width: 0px;"><div class="css-g5y9jx"><div class="v1zwn21o v1zwn21 _1psv1zeb9 _1psv1ze0 _1psv1zeif" font="default-fk-font-m" style="color: rgb(112, 112, 112); box-sizing: border-box; display: inline; white-space: pre-wrap; overflow-wrap: break-word; border-width: 0px; user-select: text; align-content: center; text-decoration-line: line-through;">27,995</div></div><div class="css-g5y9jx"><div class="v1zwn21n v1zwn20 _1psv1zeb9 _1psv1ze0" font="default-fk-font-m" style="color: rgb(51, 51, 51); box-sizing: border-box; display: inline; white-space: pre-wrap; overflow-wrap: break-word; border-width: 0px; user-select: text; align-content: center;">₹27,993</div></div></div></a></div>

price = driver.find_element(By.CSS_SELECTOR, "._1psv1zeb9._1psv1ze0._1psv1ze9x._1psv1ze7o._1psv1ze2u._1psv1ze59")
final_price = price.text.split()[0].split(",")
price = int("".join(final_price))
print(price)
# print(price.text)
# print(type(price.text))
driver.close()