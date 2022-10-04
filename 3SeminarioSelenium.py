"""
------------------------------------------
Exploracion de selenium para
-Visitar la pagina local http://venta_tickets.test
-Ingresar el correo en el input email
-Ingresar la clave en el input password
-Presionar enter
-Esperar a que cargue la pantalla principal del proyecto
-Asegurarse que exista la palabra Venta Tickets.

------------------------------------------
"""
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
