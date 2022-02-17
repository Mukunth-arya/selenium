from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")


def datainput():
    data1 = driver.get("https://davidbombal.com/")
    data2 = driver.find_element(By.LINK_TEXT, "About Us").click()
    driver.implicitly_wait(30)
    driver.back()
    driver.refresh()
    driver.forward()
#datainput()

def datavalue():
    data1 = driver.get("https://www.reddit.com/")
    data3 = driver.get_cookies()
    for i in data3:
       print(i)
datavalue()

driver.add_cookie({"name":"mukunth", "domain":"reddit.com", "value":"python"})

