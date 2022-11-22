import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestHorizontalSlider(unittest.TestCase):

    
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/dropdown"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn(self.base_url, self.driver.current_url)
        

    def test_horizontal_slider(self):
        self.menu = self.driver.find_element(By.ID,"dropdown")
        self.assertTrue(self.menu)
        self.menu.click()


        

   

    def tearDown(self):
        
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        # defaultTest="TestHorizontalSlider.test_horizontal_slider_arrow_left"
    )