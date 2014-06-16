import errno
import unittest
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

USAGE       = 'Usage: X_tests.py <Selenium hub URL> <application URL>'
RESULT_WAIT = 7

class TestSettings(object):
    AUT_URL = None
    HUB_URL = None

    @staticmethod
    def get_AUT_URL():
        return TestSettings.AUT_URL

    @staticmethod
    def get_HUB_URL():
        return TestSettings.HUB_URL


class CSDemoWebAppTests(unittest.TestCase):

    def _enter_input_numbers(self, driver, first, second):
        num1 = driver.find_element_by_id("MainContent_txbNum1")
        num2 = driver.find_element_by_id("MainContent_txbNum2")
        num1.send_keys(first)
        num2.send_keys(second)

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(TestSettings.get_HUB_URL(), webdriver.DesiredCapabilities.FIREFOX.copy())

    def tearDown(self):
        self.driver.quit()


class CSDemoWebAppFunctionalTests(CSDemoWebAppTests):

    def test_addition(self):
        test_num1, test_num2 = 2421, -964
        self.driver.get(TestSettings.get_AUT_URL())
        add = self.driver.find_element_by_id("MainContent_btnAdd")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 + test_num2)))

    def test_subtraction(self):
        test_num1, test_num2 = 140, 774
        self.driver.get(TestSettings.get_AUT_URL())
        add = self.driver.find_element_by_id("MainContent_btnSub")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 - test_num2)))

    def test_multiplication(self):
        test_num1, test_num2 = 63, 929
        self.driver.get(TestSettings.get_AUT_URL())
        add = self.driver.find_element_by_id("MainContent_btnMul")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 * test_num2)))

    def test_division(self):
        test_num1, test_num2 = 18525, 39
        self.driver.get(TestSettings.get_AUT_URL())
        add = self.driver.find_element_by_id("MainContent_btnDiv")
        self._enter_input_numbers(self.driver, test_num1, test_num2)
        add.click()
        element = WebDriverWait(self.driver, RESULT_WAIT).until(
            expected_conditions.text_to_be_present_in_element((By.ID, "MainContent_lblResult"),
                                                              str(test_num1 / test_num2)))

if __name__ == "__main__":
    if 3 > len(sys.argv):
        print USAGE
        sys.exit(errno.EINVAL)

    TestSettings.HUB_URL = sys.argv[1]
    TestSettings.AUT_URL = sys.argv[2]

    suite = unittest.TestLoader().loadTestsFromTestCase(CSDemoWebAppFunctionalTests)
    unittest.TextTestRunner().run(suite)