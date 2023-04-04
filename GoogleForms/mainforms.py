from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("D:/drivers/chromedriver.exe")
url = "https://docs.google.com/forms/d/1KcEnbrqBKfCc8XKJq-qVaKg-26kp-0GCZXdL5vzirj8/edit?pli=1"
driver.get(url)

def fillForm(name, email, zip_code, gender):
    # Replace with the path to your Chrome driver executable
    driver = webdriver.Chrome("D:/drivers/chromedriver.exe")

    # Open the Google Form URL
    driver.get("https://docs.google.com/forms/d/1KcEnbrqBKfCc8XKJq-qVaKg-26kp-0GCZXdL5vzirj8/edit?pli=1")

    # Wait until the page is fully loaded
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, 'entry.930321745')))

    # Fill out the form
    name_field = driver.find_element_by_name('entry.930321745')
    name_field.send_keys(name)

    email_field = driver.find_element_by_name('entry.2022148140')
    email_field.send_keys(email)

    zipcode_field = driver.find_element_by_name('entry.1864369405')
    zipcode_field.send_keys(zip_code)

    if gender == "Male":
        driver.find_element_by_xpath('//div[div/span[text()="Male"]]/input').click()
    else:
        driver.find_element_by_xpath('//div[div/span[text()="Female"]]/input').click()

    submit_button = driver.find_element_by_xpath('//span[text()="Submit"]')
    submit_button.click()

    driver.quit()


    
fillForm("Bohdan","bohdankvietka@gmail.com","48730","Male")
