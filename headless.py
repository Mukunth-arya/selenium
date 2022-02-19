from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By


def_value = webdriver.ChromeOptions
def_value.headless =True

driver = webdriver.Chrome(executable_path= "C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe",options = def_value)
data1 = driver.get("www.amazon.com")
print(driver.title)