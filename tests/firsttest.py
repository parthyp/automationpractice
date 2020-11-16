from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import csv

with open("../data/createAccount.csv") as createAccInfo:
    reader = csv.DictReader(createAccInfo)
    for info in reader:
        firstName = info['firstname']
        lastName = info['lastname']
        email = info['email']
        password = info['password']
        address = info['address']
        city = info['city']
        zip = info['zip']
        phone = info['phone']
        emailRef = info['emailref']
        state = info['state']




driver = webdriver.Firefox()


driver.get("http://automationpractice.com/index.php")

driver.find_element_by_class_name("login").click()
driver.find_element_by_id("email_create").send_keys(email)
driver.find_element_by_id("SubmitCreate").click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "customer_firstname"))
    )
finally:
    pass

driver.find_element_by_id("customer_firstname").send_keys(firstName)
driver.find_element_by_id("customer_lastname").send_keys(lastName)
driver.find_element_by_id("email").clear()
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("passwd").send_keys(password)


driver.find_element_by_id("firstname").send_keys(firstName)
driver.find_element_by_id("lastname").send_keys(lastName)
driver.find_element_by_id("address1").send_keys(address)
driver.find_element_by_id("city").send_keys(city)
driver.execute_script("window.scrollTo(0, 1080);")
Select(driver.find_element_by_id("uniform-id_state")).select_by_text(state)
#postcodeElement = document.find_element_by_id("postcode")
#postcodeElement.scrollIntoView()
#driver.execute_script("arguments[0].scrollIntoView();", postcodeElement)
driver.find_element_by_id("postcode").click()
driver.find_element_by_id("postcode").send_keys(zip)
driver.find_element_by_id("phone_mobile").send_keys(phone)
driver.find_element_by_id("alias").clear()
driver.find_element_by_id("alias").send_keys(emailRef)


driver.find_element_by_id("submitAccount").click()





driver.close()
