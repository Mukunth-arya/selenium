from datetime import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path = "C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
data1 = driver.get("https://github.com/")
driver.implicitly_wait(10)
data2 = driver.find_element(By.CSS_SELECTOR, "a.HeaderMenu-link.flex-shrink-0.no-underline")
data2.click()
data3 = driver.find_element(By.CSS_SELECTOR, "input#login_filed.form-control.input-block.js-login-field")
data3.send_keys("mukunthnataraj@gmail.com")
data4 = driver.find_element(By.CSS_SELECTOR, "input#password.form-control.form-control.input-block.js-password-field").send_keys("mukunth@1996")
data5 = driver.find_element(By.CSS_SELECTOR, "input.form-control+input").click()
#driver.implicitly_wait(120)
#driver.quit()