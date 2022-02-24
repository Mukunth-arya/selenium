from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

def alert():
    data1 = driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
    wait = WebDriverWait(driver, 10)
    data2 = wait.until(ec.presence_of_element_located((By.NAME, "alert")))
    data2.click()
    data3 = wait.until(ec.alert_is_present())
    print(data3.text)
    data3.accept()
    driver.close()

alert()