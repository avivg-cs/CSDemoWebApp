import errno
import unittest
import sys

from selenium import webdriver

#AUT_URL = r'http://uvo19hp0m1xqxrmfbvl.vm.cld.sr'
#HUB_URL = r'http://localhost:4444/wd/hub'
#HUB_URL = r'http://uvo1u0pa8lrfeelvyq7.vm.cld.sr:4444/wd/hub'

USAGE       = 'Usage: X_tests.py <Selenium hub URL> <application URL>'

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

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(TestSettings.get_HUB_URL(), webdriver.DesiredCapabilities.FIREFOX.copy())

    def tearDown(self):
        self.driver.close()


class CSDemoWebAppUITests(CSDemoWebAppTests):

    def test_main_page_title(self):
        self.driver.get(TestSettings.get_AUT_URL())
        self.assertIn("Home", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)

    def test_about_page_title(self):
        self.driver.get(TestSettings.get_AUT_URL() + "/About")
        self.assertIn("About", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)

    def test_contact_page_title(self):
        self.driver.get(TestSettings.get_AUT_URL() + "/Contact")
        self.assertIn("Contact", self.driver.title)
        self.assertIn("CSDemoWebApp", self.driver.title)


if __name__ == "__main__":
    if 3 > len(sys.argv):
        print USAGE
        sys.exit(errno.EINVAL)

    TestSettings.HUB_URL = sys.argv[1]
    TestSettings.AUT_URL = sys.argv[2]

    suite = unittest.TestLoader().loadTestsFromTestCase(CSDemoWebAppUITests)
    unittest.TextTestRunner().run(suite)
