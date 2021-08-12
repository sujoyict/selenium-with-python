from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\crome driver\chromedriver.exe")

driver.get("https://www.bproperty.com/")
#print(driver.title)

driver.implicitly_wait(10)

assert "Property & Real Estate for sale and for rent in Bangladesh | bproperty.com" in driver.title

driver.find_element_by_xpath('//*[@id="body-wrapper"]/div/div[1]/div/div/nav/div[2]/div/button/span[2]').click()

driver.find_element_by_name("email").send_keys("sujoyict@gmail.com")
driver.find_element_by_name("password").send_keys("abcd1234")

driver.find_element_by_xpath('//*[@id="body-wrapper"]/div/div[1]/div/div/nav/div[2]/div/div/div/div/div[1]/form/div[3]/button').click()



