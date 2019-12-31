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
import pageobject.campaignpage as campaignpage
# Locator
from locator.locators import RealmaxCompanyPageLocators
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxMainPageLocators
from locator.locators import RealmaxTagPageLocators
from locator.locators import RealmaxContactPageLocators
from locator.locators import RealmaxCampaignPageLocators
# Action
import common.actions as actions
#setting
from config.setting import *

class Contact(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)
        self.driver.implicitly_wait(10)

    #@unittest.skip("demonstrating skipping")
    def test_1_Create_New_Contact(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)

        # Add new contact
        self.driver.get(realmax_url + '/contact/detail')
        contact_page = contactpage.init(self.driver)
        contact_page.addnewcontact('sele','contact','selecontact@gmail.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        time.sleep(5)
        try:
            sele_contact = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'selecontact@gmail.com')]//td[contains(.,'selecontact@gmail.com')]")
        except NoSuchElementException:
            pass
        if len(sele_contact) > 0:
            print "Checkpoint1[Pass]: Sele contact displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Sele contact not displayed"
            exitflag = 1

        self.driver.close() 

        if exitflag == 1:
            assert False
    
    #@unittest.skip("demonstrating skipping")
    def test_2_Edit_Contact(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)

        # Edit contact
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToManageContactPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        action = actions.init(self.driver)
        action.click('contact','edit','selecontact@gmail.com')
        time.sleep(2)
        contact_page = contactpage.init(self.driver)
        contact_page.editContact('sele2','contact2','selecontact2@gmail.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        time.sleep(5)
        try:
            sele_contact = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'selecontact2@gmail.com')]//td[contains(.,'selecontact2@gmail.com')]")
        except NoSuchElementException:
            pass
        if len(sele_contact) > 0:
            print "Checkpoint2[Pass]: Sele contact 2 displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Sele contact 2 not displayed"
            exitflag = 1

        self.driver.close() 

        if exitflag == 1:
            assert False

    def test_3_Apply_Tag_To_Contact(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)
           
        
        # Apply tag to contact
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToManageContactPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        contact_page = contactpage.init(self.driver)
        contact_page.applyTagToContact('selecontact2@gmail.com', 'Realmax')

        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        contact_page.searchContact('tag','Realmax')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        time.sleep(5)
        try:
            sele_contact = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'selecontact2@gmail.com')]//td[contains(.,'selecontact2@gmail.com')]")
        except NoSuchElementException:
            pass
        if len(sele_contact) > 0:
            print "Checkpoint2[Pass]: Sele contact 2 displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Sele contact 2 not displayed"
            exitflag = 1

        self.driver.close() 

        if exitflag == 1:
            assert False

    def test_4_Delete_Contact(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)
           
        # Delete contact
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToManageContactPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        contact_page = contactpage.init(self.driver)
        contact_page.removeContact('selecontact2@gmail.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        time.sleep(5)
        try:
            sele_contact = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'selecontact2@gmail.com')]//td[contains(.,'selecontact2@gmail.com')]")
        except NoSuchElementException:
            pass
        if len(sele_contact) == 0:
            print "Checkpoint2[Pass]: Sele contact 2 not displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Sele contact 2 displayed"
            exitflag = 1

        self.driver.close() 

        if exitflag == 1:
            assert False