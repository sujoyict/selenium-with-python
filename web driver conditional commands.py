from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("http://facebook.com")

element = driver.find_element_by_name("email")

print(element.is_displayed())
print(element.is_enabled())

element = driver.find_element_by_name("pass")

print(element.is_displayed())
print(element.is_enabled())