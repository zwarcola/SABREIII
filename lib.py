import requests
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def login(credentials):
    user = credentials['username']
    pwd = credentials['password']

    driver = webdriver.Chrome(executable_path = '/chromedriver.exe')
    driver.get(URL)

    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://google.com/ncr")
        driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
        first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
        print(first_result.get_attribute("textContent"))

login()
