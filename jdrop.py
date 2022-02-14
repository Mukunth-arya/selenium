from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")

def newdriver(web_field, value):
    for data in data2:
        print(data.text)
        for i in range(len(value)):
            print(len(value))

            if data.text == value[i]:
             data.click()
             break


GET = driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
data1 = driver.find_element(By.ID, "justAnInputBox")
data1.click()
data2 = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
data_key = ["choice 2", "choice 3", "choice 4", "choice 7" "choice 8"]
#data_key = ["all"]
newdriver(data2, data_key)
driver.implicitly_wait(30)

driver.quit()