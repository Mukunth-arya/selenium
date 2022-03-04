import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe" )

data4 = driver.get("https://github.com/")
data5 = driver.find_element(By.LINK_TEXT, "Sign in").click()
data6 = driver.find_element(By.XPATH, "input[@name='login']")
data7 = driver.find_element(By.CSS_SELECTOR, "input#password")
data1 = xlrd.open_workbook("sample.xls")
sheet = data1.sheet_by_name("myfile")

rowscount = sheet.nrows
colcount = sheet.ncols

print (rowscount)
print (colcount)


for datas in range (0 , rowscount):
    data3 = sheet.cell_value(datas, 0)
    data8 = sheet.cell_value(datas, 1)
    data6.send_keys(data3)
    data7.send_keys(data8)
    driver.find_element(By.NAME, "commit").click()