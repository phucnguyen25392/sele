import unittest
import lib.HTMLTestRunner as HTMLTestRunner
import pageobject.loginpage as loginpage
from locator.locators import RealmaxLoginPageLocators
from selenium import webdriver

#setting
from config.setting import *

class ValidLogin(unittest.TestCase):
      
    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.get(realmax_url)

    def test(self):
        
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
        login_page.wait(2)
        # Check point ---
        realmax_img = self.driver.find_element(*RealmaxLoginPageLocators.realmax_img)
        assert realmax_img.is_displayed()
        #----------------
        login_page.logout()

    def tearDown(self):
        self.driver.close()

class InvalidLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.get(realmax_url)

    def test(self):
        
        login_page = loginpage.init(self.driver)
        login_page.login('admin@123.com', 'abc123')
        login_page.wait(2)
        # Check point ---
        loginfailed = self.driver.find_element(*RealmaxLoginPageLocators.loginfailed_mess)
        assert loginfailed.is_displayed()
        #----------------
        login_page.logout()

    def tearDown(self):
        self.driver.close()