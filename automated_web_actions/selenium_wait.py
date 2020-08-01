from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PATH = r'C:\Users\132392\PycharmProjects\natural-language-processing\chromedriver.exe'

url = 'https://www.google.com/earth/'
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get(url)

wait = WebDriverWait(driver, 10)
launch_earth = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launch_earth.click()
