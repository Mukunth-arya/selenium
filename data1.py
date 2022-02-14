from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\mukunth\\PycharmProjects\\pythonProject\\mypackage\\chromedriver.exe")



#def datastream(value):
#    send1 = driver.get("http://demo.automationtesting.in/Alerts.html")
#    send2 = driver.find_element(By.CSS_SELECTOR, datastream1 ).click()
#    driver.implicitly_wait(5)
#    alert1 = driver.switch_to_alert
#    print(alert1.text)
#    alert1.accept()

#datastream1 = "button.btn.btn-danger"
#datastream(datastream1)
#driver.implicitly_wait(20)
#driver.quit()


##second selectform

#def keyvalue():
#    send1 = driver.get("http://demo.automationtesting.in/Frames.html")
#    send2 = driver.find_element(By.CSS_SELECTOR, "a.analystic").text
#    print(send2)
#
#    driver.switch_to.default_content()
#    driver.switch_to.parent_frame()

#keyvalue()
def keyvalue2():
    send1 = driver.get("https://online2pdf.com/pdf2word")
    send2 = driver.find_element(By.XPATH, "button[@type='button']")
    send2.send_keys("C:\\Users\\mukunth\\execution3.json")
    send2.click()
keyvalue2()
### some cases if you have router there the username and password are pop up before enter into config menu in that case do below steps
#https://admin:admin@"desired url"

