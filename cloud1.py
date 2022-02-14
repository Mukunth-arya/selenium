from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

get_url = driver.get("https://github.com/")
wait = driver.implicitly_wait(10)
send_data = driver.find_element(By.LINK_TEXT, "Sign in")
send_data.click()
#signin_now = driver.find_element(By.ID, "login_field").send_keys("mukunthnataraj@gmail.com")
signin_now = driver.find_element(By.CLASS_NAME, "form-control.input-block.js-login-field").send_keys("mukunthnataraj@gmail.com")
passwd = driver.find_element(By.ID, "password").send_keys("arya")
click_n = driver.find_element(By.NAME, "commit")
click_n.click()


time.sleep(5)
driver.quit()