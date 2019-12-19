# -*- coding: utf-8 -*-

import unittest
import time
import lib.HTMLTestRunner as HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support import expected_conditions as EC
# Page 
import pageobject.loginpage as loginpage
import pageobject.dashboardpage as dashboardpage
import pageobject.companypage as companypage
# Locator
from locator.locators import RealmaxCompanyPageLocators
from locator.locators import RealmaxMainPageLocators
#setting
from config.setting import *

class InsertValidCompany(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.get("https://www.realmax.ga")

    def test(self):

        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')

        # Navigate to company page
        time.sleep(2)
        company_page = companypage.init(self.driver)
        company_page.addnewcompany('sele', 'test', '', '', '134, Le loi, P, Ben Thanh', 'https://www.robotics.org/', '0903453756', 'Your 1 Online Resource for Industrial Robotics')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        verify_sele_text = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'sele')]")
        # Check "Verify" text is shown in sele company info line
        assert verify_sele_text.is_displayed()

        ######################
        #                    #
        #    Clean up        #
        #                    #
        ###################### 
        del_sele_link =  self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'sele')]//span[@title='Remove']")
        del_sele_link.click()
        time.sleep(2)
        confirm_delete_ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.confirm_delete_ok_btn)
        confirm_delete_ok_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()

    def tearDown(self):
        self.driver.close() 



        
