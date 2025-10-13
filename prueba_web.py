from selenium import webdriver
import time 

driver = webdriver.Chrome ()
driver.implicitly_wait (5)

try:
    #LOGIN
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
