from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("https://www.rvkcars.com/")
time.sleep(5)
print(driver.title)  #FR

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)  #TT

driver.back()

time.sleep(5)
print(driver.title) #FR

driver.forward()

time.sleep(5)
print(driver.title)  #TT

driver.quit()
