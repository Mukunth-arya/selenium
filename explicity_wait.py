from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

def explicit():
    data1 = driver.get("https://www.docker.com/")
    wait = WebDriverWait(driver, 10)
    link = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Sign In")))
    link.click()
    email_id = wait.until(ec.presence_of_element_located((By.ID, "username")))
    email_id.send_keys("mukunthnataraj@gmail.com")
explicit()