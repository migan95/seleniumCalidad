import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgBusqueda(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_seminario(self):
        driver = self.driver
        driver.get('http://venta_tickets.test')
        self.assertIn("Login",driver.title)
        elem = driver.find_element(By.NAME,"email")
        elem.clear()
        elem.send_keys('admin@test.com')
        elem = driver.find_element(By.NAME, "password")
        elem.clear()
        elem.send_keys('admin')
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver,3) #Agregamos pausa para permitir que la aplicacion cambie de pagina
        elem = wait.until(EC.presence_of_element_located((By.ID,'wrapper')))
        URL = driver.current_url
        self.assertEquals(URL,'http://venta_tickets.test/')

    def test_logout_seminario(self):
        driver = self.driver
        driver.get('http://venta_tickets.test')
        self.assertIn("Login",driver.title)
        elem = driver.find_element(By.NAME,"email")
        elem.clear()
        elem.send_keys('admin@test.com')
        elem = driver.find_element(By.NAME, "password")
        elem.clear()
        elem.send_keys('admin')
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver,3) #Agregamos pausa para permitir que la aplicacion cambie de pagina
        elem = wait.until(EC.presence_of_element_located((By.ID,'wrapper')))
        elem = driver.find_element(By.XPATH, '//a[@href="http://venta_tickets.test/logout"]')
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.ID, 'email')))
        URL = driver.current_url
        self.assertEquals(URL,'http://venta_tickets.test/login')

    def test_navegacion_perfil_seminario(self):
        driver = self.driver
        driver.get('http://venta_tickets.test')
        self.assertIn("Login", driver.title)
        elem = driver.find_element(By.NAME, "email")
        elem.clear()
        elem.send_keys('admin@test.com')
        elem = driver.find_element(By.NAME, "password")
        elem.clear()
        elem.send_keys('admin')
        elem.send_keys(Keys.RETURN)
        wait = WebDriverWait(driver, 3)  # Agregamos pausa para permitir que la aplicacion cambie de pagina
        elem = wait.until(EC.presence_of_element_located((By.ID, 'wrapper')))
        elem = driver.find_element(By.XPATH,'//*[@id="accordionSidebar"]/li[2]/a')
        elem.click()
        elem = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/h3')))
        self.assertEquals(elem.text,'Perfil de Usuario')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()