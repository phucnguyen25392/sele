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

class Permission(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test_1_Check_User_Permission(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_user, gb_user_pass)

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        self.driver.get(realmax_url + '/admin/user/detail')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint1[Pass]: User cannot create user"
            assert True
        else:
            print "Checkpoint1[Failed]: User cannot create user"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/user/myProfile')
        if self.driver.title == 'User':
            print "Checkpoint2[Pass]: User can edit user"
            assert True
        else:
            print "Checkpoint2[Failed]: User cannot edit user"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/user/list')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint3[Pass]: User cannot list user"
            assert True
        else:
            print "Checkpoint3[Failed]: User can list user"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/company/detail/15')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint4[Pass]: User cannot update company"
            assert True
        else:
            print "Checkpoint4[Failed]: User can update company"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/list')
        if self.driver.title == 'Manage campaign':
            print "Checkpoint5[Pass]: User can list campaign"
            assert True
        else:
            print "Checkpoint5[Failed]: User cannot list campaign"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/detail')
        time.sleep(3)
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint6[Pass]: User cannot create campaign"
            assert True
        else:
            print "Checkpoint6[Failed]: User can create campaign"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/detail/33404')
        time.sleep(3)
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint7[Pass]: User cannot update campaign"
            assert True
        else:
            print "Checkpoint7[Failed]: User can update campaign"
            exitflag = 1

        self.driver.quit()

        if exitflag == 1:
            assert False

    def test_2_Check_Admin_Permission(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        self.driver.get(realmax_url + '/admin/user/detail')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint1[Failed]: Admin cannot create user"
            exitflag = 1
        else:
            print "Checkpoint1[Pass]: Admin can create user"
            assert True

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/user/myProfile')
        if self.driver.title == 'User':
            print "Checkpoint2[Pass]: Admin can edit user"
            assert True
        else:
            print "Checkpoint2[Failed]: Admin cannot edit user"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/user/list')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint3[Failed]: Admin cannot list user"
            exitflag = 1
        else:
            print "Checkpoint3[Pass]: Admin can list user"
            assert True

        time.sleep(3)
        self.driver.get(realmax_url + '/admin/company/detail/15')
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint4[Failed]: Admin cannot update company"
            exitflag = 1
        else:
            print "Checkpoint4[Pass]: Admin can update company"
            assert True

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/list')
        if self.driver.title == 'Manage campaign':
            print "Checkpoint5[Pass]: Admin can list campaign"
            assert True
        else:
            print "Checkpoint5[Failed]: Admin cannot list campaign"
            exitflag = 1

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/detail')
        time.sleep(3)
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint6[Failed]: Admin cannot create campaign"
            exitflag = 1
        else:
            print "Checkpoint6[Pass]: Admin can create campaign"
            assert True

        time.sleep(3)
        self.driver.get(realmax_url + '/campaign/detail/33404')
        time.sleep(3)
        url = self.driver.current_url
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint7[Failed]: Admin cannot update campaign"
            exitflag = 1
        else:
            print "Checkpoint7[Pass]: Admin can update campaign"
            assert True

        self.driver.quit()

        if exitflag == 1:
            assert False