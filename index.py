from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import urllib.request
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager(version="98.0.4758.102").install())
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')
search.send_keys('people wearing mask',Keys.ENTER)

elem = driver.find_element_by_link_text('Images')
elem.get_attribute('href')
elem.click()

