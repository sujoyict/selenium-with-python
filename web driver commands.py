from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("https://evaly.com.bd/")

#driver.find_element_by_xpath("/html/body/reach-portal[1]/div/div/div/section/div/button/svg/path").click()


#alert = driver.switch_to.alert
#print(alert.text)
#alert.accept()
#alert.dismiss()
#driver.find_element_by_css_selector("#ImageUpload [type=file]").send_keys('/static/images/efood/efood-banner.png')
time.sleep(5)
#driver.find_element_by_xpath ("//*[@id='react-toast']/html/body/reach-portal[1]/div/div/div/section/div/button/svg").click()
#driver.find_element_by_xpath ("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
driver.find_element_by_xpath('//button[@class="absolute top-0 right-0 p-2 text-black"]').click()
time.sleep(5)
driver.find_element_by_xpath('//button[@class="flex items-center"]').click()

driver.find_element_by_xpath("//body/div[@id='custom-popover']/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()


#elem = driver.find_element_by_class_name("currentColor")
#ac = ActionChains(driver)
#ac.move_to_element(elem).click().perform()
#driver.switch_to_default_content()
#driver.switch_to_alert().dismiss()

#element = driver.find_element_by_name("phone")

#print(element.is_displayed())

#print(element.is_enabled())