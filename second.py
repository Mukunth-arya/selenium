from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import time
value = "chrome"
driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

if value == "chrome":
    driver.get("https://github.com/login")
    driver.find_element(By.ID, "login_field").send_keys("mukunthnataraj@gmail.com")
    driver.find_element(By.ID, "password").send_keys("mukunth@1996")
    driver.find_element(By.NAME, "commit").click()
else:
    print("enter the correct module")




