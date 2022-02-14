from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

def mydriver():

    get_url = driver.get("https://www.aisa.sch.ae/admissions/apply-for-admission/online-application-form")
    send1 = driver.find_element(By.ID, "field_14_3765")
    send1.send_keys("mukuntharya")
    send2 = driver.find_element(By.ID, "field_15_3765")
    send2.send_keys("mukuntharya")
def selectvalue():
    select1 = driver.find_element(By.ID, "field_18_3765")
    select2 = Select(select1)
    data = select2.select_by_visible_text("India")
    data.click()

mydriver()
selectvalue()
key = driver.find_element(By.ID, "field_18_3765")

