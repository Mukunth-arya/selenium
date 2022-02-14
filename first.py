from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import time

driver = webdriver.Chrome("C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")
driver.get("http://google.com")
driver.find_element(By.NAME, "q").send_keys("polimenews")
print(driver.title)
selector = driver.find_element(By.CSS_SELECTOR, "ul.bw4e9b li span")
selector.click()
time.sleep(6)
driver.quit()