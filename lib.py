import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.chrome.options import Options

LOGIN_REDIRECT_URL = 'https://paws.tcnj.edu/psp/paws/?cmd=login&languageCd=ENG&'
URL = 'https://paws.tcnj.edu'

def login(credentials):
    #begin login process
    user = credentials['username']
    pwd = credentials['password']

    #hide chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)

    #await redirect from chrome driver
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
        return -1

    html_source = driver.page_source

    print('Login sucess!')
    time.sleep(2)

    return driver

def searchCourse(credentials, driver):
    try:
        print("Searching for course...")
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

        #select term and year
        termSelect = driver.find_element_by_xpath('//*[@id="CLASS_SRCH_WRK2_STRM$35$"]')
        termSelect.click()
        time.sleep(0.2)
        Found = False
        for option in termSelect.find_elements_by_tag_name('option'):
            if option.get_attribute('innerHTML') == (credentials['year'] + ' ' + credentials['semester']):
                time.sleep(0.1)
                Found = True
                option.click()
                break

        if not Found:
            print('ERROR FINDING YEAR AND SEMESTER')

        time.sleep(0.2)

        #Select the proper course subject
        courseSelect = driver.find_element_by_xpath("//select[@id='SSR_CLSRCH_WRK_SUBJECT_SRCH$0']")
        courseSelect.click()
        time.sleep(0.2)
        Found = False
        for option in courseSelect.find_elements_by_tag_name('option'):
            if option.get_attribute('value') == credentials['subject']:
                time.sleep(0.1)
                Found = True
                option.click()
                break

        if not Found:
            print('ERROR FINDING CLASS SUBJECT')

        time.sleep(0.2)

        #Enter course number
        courseNum = driver.find_element_by_name('SSR_CLSRCH_WRK_CLASS_NBR$7')
        courseNum.send_keys(credentials['class_num'])
        courseNum.send_keys(Keys.RETURN)
        time.sleep(2)

        #open the class info
        classLink = driver.find_element_by_link_text(credentials['class_num'])
        classLink.click()
        time.sleep(2)

        print("Getting total seats...")
        #get amount of availible seats
        availibleSeats = driver.find_element_by_xpath('//*[@id="win0divSSR_CLS_DTL_WRK_AVAILABLE_SEATS"]')
        availibleSeats = availibleSeats.find_element_by_class_name('PSEDITBOX_DISPONLY').get_attribute('innerHTML')

        #get class title
        classTitle = driver.find_element_by_xpath('//*[@id="DERIVED_CLSRCH_DESCR200"]')
        classTitle = driver.find_element_by_class_name('PALEVEL0SECONDARY').get_attribute('innerHTML')

        classTitle = classTitle.replace("&nbsp;", "")


    except:
        print("ERROR WHILE FINDING COURSE")
        return -1

    print("Done!")
    #return total number
    return [availibleSeats, classTitle]
