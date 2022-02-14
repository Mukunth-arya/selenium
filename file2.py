from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

driver.get("https://en.wikipedia.org/wiki/Main_Page")
data3 = driver.find_elements(By.CSS_SELECTOR, "u1.vector-menu-content-list>li:nth-of-type(n) --all")
for i in data3:
    if i.text == "Wikimedia Commons":
        i.click()
