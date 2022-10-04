
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://venta_tickets.test')
assert "Login" in driver.title
elem = driver.find_element(By.NAME,"email")
elem.clear()
elem.send_keys('admin@test.com')
elem = driver.find_element(By.NAME, "password")
elem.clear()
elem.send_keys('admin')
elem.send_keys(Keys.RETURN)
assert "Venta Tickets" in driver.page_source
#driver.close()
