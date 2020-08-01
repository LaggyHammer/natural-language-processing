from selenium import webdriver

PATH = r'C:\Users\132392\PycharmProjects\natural-language-processing\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
message_field = driver.find_element_by_xpath('//*[@id="user-message"]')
message_field.send_keys('Big Brother is watching (0_0)')
show_message_button = driver.find_element_by_xpath('//*[@id="get-input"]/button')
show_message_button.click()

a_field = driver.find_element_by_xpath('//*[@id="sum1"]')
a_field.send_keys('10')
b_field = driver.find_element_by_xpath('//*[@id="sum2"]')
b_field.send_keys('49')
show_sum_button = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
show_sum_button.click()

