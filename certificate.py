from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

data1 = Options()
data1.add_argument("--allow-running-insecure-content")
data1.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe", options= data1)
driver.get("https://expired.badssl.com")
data2 = driver.find_element(By.TAG_NAME,"h1").text
print (data2)