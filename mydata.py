from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
driver.get("https://ucp.org.in/")
data = driver.find_elements(By.TAG_NAME, "img")
#for i in data:
#    display = i.text
#    print(display)
#    print("here represents the data:", i.get_attribute("href"))

for t in data:
     display = t.text
     print(display)
     print(t.get_attribute("src"))


time.sleep(9)
driver.close()