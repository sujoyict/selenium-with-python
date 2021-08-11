from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("https://evaly.com.bd/")
driver.implicitly_wait(10)

#popup close
driver.find_element_by_xpath('//button[@class="absolute top-0 right-0 p-2 text-black"]').click()

#login execution
driver.find_element_by_xpath('//button[@class="flex items-center"]').click()
driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
#driver.find_element_by_xpath('//*[@id="body-wrapper"]/div/div[1]/div/div/nav/div[2]/div/button/span[2]').click()
driver.find_element_by_name("phone").send_keys("01721693036")
driver.find_element_by_name("password").send_keys("Dhaka_71%")
time.sleep(2)
#driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
driver.find_element_by_xpath("//*[@id='custom-popover']/div/div/div/form/div[3]/button").click()
#driver.find_element_by_xpath('//[@class="flex items-center justify-between py-3 text-sm"]').click()


#open speaker page
time.sleep(2)
driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div/div[1]/div/ul/li[9]/a").click()

#print all brands name
br_name = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div[2]/div/div/div").text
print(br_name)

#open brand mi
time.sleep(2)
driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div[1]/div[2]/div/div/div/a[1]/div/div[1]").click()

#print mi brand category details
time.sleep(2)
mi_cat = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div[3]/div/div[3]").text
print(mi_cat)



driver.close()
