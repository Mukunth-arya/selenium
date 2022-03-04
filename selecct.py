from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")


def class1 ():
    get_v = driver.get("https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022")
    driver1 = driver.find_element(By.CLASS_NAME, "heading3.resourceName.expandedEva1lh1.x-hidden-focus")
    driver1.click()
    driver2 = driver.find_element(By.CLASS_NAME, "icon-accordion.x-hidden-focus")
    driver2.click()
    driver3 = driver.find_elements(By.CSS_SELECTOR, "#divMultipleFileTypes > fieldset > p > label:nth-child(8)")
    driver3.click()
    driver4 = driver.find_element(By.ID, "btnRegisterWithFileTypes")
    driver4.click()ver

    send1 = driver.find_element(By.ID,  "marketoFirstName")
    send1.send_keys("Mukunth")
    send2 = driver.find_element(By.ID, "marketoLastname")
    send2.send_keys("Arya")
    send3 = driver.find_element(By.ID, "marketoCompany")
    send3.send_keys("uit-college")
    send4 = driver.find_element(By.ID, "marketoCompanySize")
    select_keys = Select(send4)
    select_keys.select_by_value("2-4")
    select_keys2 = Select(send4)
    select_keys2.select_by_value("Business Executive")
    send4 = driver.find_element(By.ID, "marketoEmail")
    send4.send_keys("mukunthnataraj@gmail.com")
    send5 = driver.find_element(By.id, "marketoPhone")
    send5.send_keys("9500618719")
    new("india")
    send6 = driver.find_elements(By.id, "btnMarkettoContinue")
    send6.click()
class1()



def new(values):
    new_data = driver.find_element(By.id, "marketoCountry")
    for i in new_data:
        print(len(i))
        if i == "values":
            i.click()
            break

