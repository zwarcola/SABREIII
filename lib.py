import requests
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options

LOGIN_REDIRECT_URL = 'https://paws.tcnj.edu/psp/paws/?cmd=login&languageCd=ENG&'
URL = 'https://paws.tcnj.edu'

credentials = {
    'username' : 'warcolz1',
    'password' : 'Sugaree1!',
    "subject": 'CSC',
    "class_num": '41817',
    "year": '',
    "semester": '',
    "carrier": '',
    "phone_num": '',
    "email": '',
    "notif": '',
    "time": ''
}

def login(credentials):
    #begin login process
    user = credentials['username']
    pwd = credentials['password']

    # chrome_options = Options()
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome() #options=chrome_options
    driver.get(URL)

    while True:
        time.sleep(2)
        if LOGIN_REDIRECT_URL == driver.current_url:
           print("Opening...")
           break;

    try:
        print('Attempting Login...')
        #get username field
        loginForm = driver.find_element_by_xpath('//*[@id="userid"]')
        loginForm.send_keys(user)

        #get password field
        passwordForm = driver.find_element_by_xpath('//*[@id="pwd"]')
        passwordForm.click()
        passwordForm.send_keys(pwd)

        #get submit button
        submit = driver.find_element_by_xpath('//*[@name="submit"]')
        submit.click()
        print("Logging in...")
    except:
        print("ERROR GETTING LOGIN FORM / LOGGING IN!!!")

    html_source = driver.page_source

    print('Login sucess!')
    time.sleep(2)

    return driver

def searchCourse(credentials, driver):
    #Navigate to Student Center
    link = driver.find_element_by_link_text('Student Center')
    link.click()
    time.sleep(0.2)

    #Open search menu
    driver.switch_to.frame(driver.find_element_by_name('TargetContent'))
    search = driver.find_element_by_link_text('Search') #DERIVED_SSS_SCL_SSS_GO_4$83$
    search.click()
    time.sleep(3)

    #Uncheck "Show Open Classes Only"
    closed = driver.find_element_by_name("SSR_CLSRCH_WRK_SSR_OPEN_ONLY$3")
    closed.click()
    time.sleep(0.2)

    #Select the proper course subject
    courseSelect = driver.find_element_by_xpath("//select[@id='SSR_CLSRCH_WRK_SUBJECT_SRCH$0']")
    courseSelect.click()
    time.sleep(0.2)
    for option in courseSelect.find_elements_by_tag_name('option'):
        if option.get_attribute('value') == credentials['subject']:
            print(option.get_attribute('value'))
            time.sleep(0.1)
            option.click()
            break
    time.sleep(0.2)

    #Enter course number
    courseNum = driver.find_element_by_name('SSR_CLSRCH_WRK_CLASS_NBR$7')
    courseNum.send_keys(credentials['class_num'])
    time.sleep(0.5)
    window.send_keys(u'\ue007')
    time.sleep(2)

driver = login(credentials)
searchCourse(credentials, driver)
time.sleep(10)
driver.close()
