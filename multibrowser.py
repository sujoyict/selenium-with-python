from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("http://www.seleniumframework.com/python-course/")

print(driver.title)

print(driver.current_url)

#print(driver.page_source)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/h2[1]/a/input").click()

time.sleep(5)

driver.close()