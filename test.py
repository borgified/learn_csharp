from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os

desired_cap = {
 'browserName': 'android',
 'device': 'Samsung Galaxy S8',
 'realMobile': 'true',
 'os_version': '7.0'
}

username=os.environ.get('BROWSERSTACK_USERNAME')
access_key=os.environ.get('BROWSERSTACK_ACCESS_KEY')

driver = webdriver.Remote(
    command_executor='http://{}:{}@hub.browserstack.com:80/wd/hub'.format(username,access_key),
    desired_capabilities=desired_cap)

driver.get("http://www.bing.com")
if not "Bing" in driver.title:
    raise Exception("Unable to load bing page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print driver.title
driver.quit()
