import unittest
import time
import lib.HTMLTestRunner as HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# Page 
import pageobject.loginpage as loginpage
import pageobject.dashboardpage as dashboardpage
import pageobject.companypage as companypage
import pageobject.userpage as userpage
import pageobject.contactpage as contactpage
import pageobject.tagpage as tagpage
# Locator
from locator.locators import RealmaxCompanyPageLocators
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxMainPageLocators
from locator.locators import RealmaxTagPageLocators
from locator.locators import RealmaxContactPageLocators
# Action
import common.actions as actions
#setting
from config.setting import *

class Tag(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test_Apply_Tag_To_Contact_And_User(self):
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)

        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetouserpage()

        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page = userpage.init(self.driver)
        user_page.appplyTagToUser('phucnguyen25392+seleuser@gmail.com', 'Realmax')
        
        # Add new contact apply tag
        time.sleep(2)
        dashboard_page.navigateToManageContactPage()
        time.sleep(2)
        contact_page = contactpage.init(self.driver)
        contact_page.searchContact('phucnguyen25392+seleuser@gmail.com')
        contact_page.applyTagToContact('phucnguyen25392+seleuser@gmail.com', 'Realmax')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        self.driver.get(realmax_url + "/logout")
        login_page.login(gb_user, gb_user_pass)
        dashboard_page.navigateToTagPage()
        time.sleep(3)
        try:
            realmax_tag = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'Realmax')]")
        except NoSuchElementException:
            pass
        if len(realmax_tag) > 0:
            print "Checkpoint1[Pass]: Realmax tag displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Realmax tag not displayed"
            exitflag = 1
        
        action = actions.init(self.driver)
        action.click('tag', 'apply_contact', 'Realmax')
        time.sleep(5)
        try:
            sele_contact = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//label[contains(.,'Seleuser User')]")
        except NoSuchElementException:
            pass
        if len(sele_contact) > 0:
            print "Checkpoint2[Pass]: Seleuser contact displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Seleuser contact not displayed"
            exitflag = 1
        time.sleep(5)
        save_btn = self.driver.find_element(*RealmaxTagPageLocators.save_btn)
        save_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxTagPageLocators.ok_btn)
        ok_btn.click()

        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        
        tag_page = tagpage.init(self.driver)
        tag_page.removeContagInTag('Realmax', 'Seleuser User')
        self.driver.get(realmax_url + "/logout")

        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page = userpage.init(self.driver)
        user_page.removeAllTagsInUser('phucnguyen25392+seleuser@gmail.com')

        if exitflag == 1:
            assert False

    def tearDown(self):
        self.driver.close() 

