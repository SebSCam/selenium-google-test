from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import unittest

class TestGoogle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Inicio Prueba")
        cls.DRIVER_PATH = "/home/sebscam/Documentos/selenium-test-python/web-driver/chromedriver"
        cls.URL = "https://www.google.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = self.DRIVER_PATH)
        self.driver.get(self.URL)
     
    def tearDown(self):
        print("bye!")
        self.driver.close()

    def test(self):
        element = self.driver.find_element(By.NAME , "q")
        element.send_keys("Pruebas")
        element.submit()
        time.sleep(3)

        title = self.driver.title
        
        print(title)

if __name__ == '__main_' :
    unittest.main()