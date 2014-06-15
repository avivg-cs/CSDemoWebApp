import unittest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

RESULT_WAIT = 7

class CSDemoWebAppTests(unittest.TestCase):
    
    def _enter_input_numbers(self, driver, first, second):
        num1 = driver.find_element_by_id("MainContent_txbNum1")
        num2 = driver.find_element_by_id("MainContent_txbNum2")
        num1.send_keys(first)
        num2.send_keys(second)
    
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_main_page_title(self):
        self.driver.get("localhost:11975")
        self.assertIn("Home", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)
        
    def test_about_page_title(self):
        self.driver.get("localhost:11975/About")
        self.assertIn("About", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)
    
    def test_contact_page_title(self):
        self.driver.get("localhost:11975/Contact")
        self.assertIn("Contact", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)
    
    def test_addition(self):
        test_num1, test_num2 = 2421, -964
        self.driver.get("localhost:11975")
        add = self.driver.find_element_by_id("MainContent_btnAdd")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 + test_num2)))
    
    def test_subtraction(self):
        test_num1, test_num2 = 140, 774
        self.driver.get("localhost:11975")
        add = self.driver.find_element_by_id("MainContent_btnSub")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 - test_num2)))
    
    def test_multiplication(self):
        test_num1, test_num2 = 63, 929
        self.driver.get("localhost:11975")
        add = self.driver.find_element_by_id("MainContent_btnMul")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 * test_num2)))
    
    def test_division(self):
        test_num1, test_num2 = 18525, 39
        self.driver.get("localhost:11975")
        add = self.driver.find_element_by_id("MainContent_btnDiv")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 / test_num2)))
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()