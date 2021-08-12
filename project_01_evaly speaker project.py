from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")
print("-----Connecting to Evaly Website \n")
driver.get("https://evaly.com.bd/")
driver.maximize_window()
wait_time=10
driver.implicitly_wait(wait_time)

#popup close
print("-----Popup close \n")
driver.find_element_by_xpath('//button[@class="absolute top-0 right-0 p-2 text-black"]').click()

#login execution
print("-----Login execution start \n")
driver.find_element_by_xpath('//button[@class="flex items-center"]').click()
driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
#driver.find_element_by_xpath('//*[@id="body-wrapper"]/div/div[1]/div/div/nav/div[2]/div/button/span[2]').click()
driver.find_element_by_name("phone").send_keys("01721693036")
driver.find_element_by_name("password").send_keys("Dhaka_71%")
time.sleep(2)
#driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/div/form/div[3]/button").click()
#driver.find_element_by_xpath('//[@class="flex items-center justify-between py-3 text-sm"]').click()
print("-----Login successful\n")

#open speaker page
time.sleep(2)
print("-----Open all brand page \n")
driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div/div[1]/div/ul/li[9]/a").click()

#print all brands name
print("-----Print all brands name \n")
br_name = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div[2]/div/div/div").text
print(br_name)

#open brand mi
print("-----Open Brand Mi \n")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div[2]/div/div/div/a[1]/div/div[1]").click()

#print mi brand category details
time.sleep(2)
print("-----Print all category name & price of Brand Mi \n")
#productInfoList = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/div/div[3]/a[1]/div').text

#print(productInfoList)
#productName = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/div/div[3]/a[1]/div/div[2]/p').text
#print(productName)
#productName = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div/div[3]/a[1]/div/div[2]/p").text
#productPrice = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div/div[3]/a[1]/div/div[3]/p[2]").text
#print(productPrice)

#for values in productInfoList:
#    print(values)

name1 = []
price1 = []
#productprice=driver.find_elements_by_xpath('//p[@class="Card___StyledP2-sc-1629dl9-1 cFzjHk"]')
productprice=driver.find_elements_by_xpath('//div[@class="p-4 pt-0"]//p')
productname=driver.find_elements_by_xpath('//p[@class="Card___StyledP4-sc-1629dl9-4 fWEsJX text-sm text-gray-800"]')
for price in productprice:
    print(price.text)
    price1.append(price.text)
for name in productname:
    print(name.text)
    name1.append(name.text)


#open career option
time.sleep(2)
print("-----Page scrolling & open career option \n")
career = driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[6]/div/div[1]/div[2]/ul/li[5]/a')
driver.execute_script("arguments[0].scrollIntoView();",career)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[6]/div/div[1]/div[2]/ul/li[5]/a').click()

#expand= driver.find_element_by_xpath('//*[@id="__next"]/div[1]/div[3]/div/div[2]/div[1]/div[4]/div/span/svg')
#select(expand)








#for pp in productPrice:
    #print(pp.text)


#links = driver.find_elements(By.TAG_NAME,"a")
#print(len(links))
#prods=driver.find_elements(By.PARTIAL_CLASS_NAME, "Card___Styled")
#prods=
#for prod in prods:
    #print(prod.text)



#for link in links:
    #print(link.text)


#for el in productInfoList:

#temp_Item = {'productName': productName,
            # 'productPrice': productPrice}

#print(temp_Item)

#productPrice_list = [productPrice]

#max_price = max(productPrice_list)
#print(max_price)
#for item in r['items']:
    #productName.append(item['name'])
    #productPrice.append(item['price_max'])



#for i in tqdm(listOflinks):


#Shopee = pd.DataFrame(zip(titles_list, prices_list), columns=[‘ItemName’, ‘Price’])

#for val in mi_cat

#driver.close()
