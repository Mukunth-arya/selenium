from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import time

driver = webdriver.Chrome("C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
driver.implicitly_wait(10)
def data1():
    data1 = driver.get("https://en.wikipedia.org/wiki/Main_Page")
    print(driver.title)
    data2 = driver.find_element(By.LINK_TEXT, "View source").click()


data1()
