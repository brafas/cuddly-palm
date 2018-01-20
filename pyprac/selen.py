from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox() # instance of Firefox Webdriver is created
driver.get("http://www.python.org") # get() method will navigate to page. Waits until page loaded. 'onload' event fired.
assert "Python" in driver.title # simple way to end if the title doesn't have python in it
elem = driver.find_element_by_name("q") # Webdriver offers few ways to find elements using find_element_by_* methods.
elem.clear() # To be safe, wee clear any prepopulated text in search field.
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()