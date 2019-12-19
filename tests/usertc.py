import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# Page 
import pageobject.loginpage as loginpage
import pageobject.dashboardpage as dashboardpage
import pageobject.companypage as companypage
import pageobject.userpage as userpage
# Locator
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxMainPageLocators
#setting
from config.setting import *

class RootUserCreateAdminAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
    
    def test(self):
        # Navigate to user manage page
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetouserpage()
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('sele','sele','Robotic','Administrator','sele@gmail.com','Test@123','Test@123','0904536477')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))

        ######################
        #                    #
        ###   Checkpoint   ###
        #                    #
        ######################
        viewlength_sb = Select(self.driver.find_element(*RealmaxUserPageLocators.viewlength_sb))
        viewlength_sb.select_by_visible_text('All')
        verify_sele_text = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'sele')]//td[contains(.,'Administrator')]")
        # Check create user success
        assert verify_sele_text.is_displayed()
        self.driver.get(realmax_url + "/logout")
        login_page = loginpage.init(self.driver)
        login_page.login('sele@gmail.com', 'Test@123')
        time.sleep(5)
        admin_link = self.driver.find_element(*RealmaxMainPageLocators.admin_link)
        admin_link.click()
        time.sleep(2)
        user_link = self.driver.find_element(*RealmaxMainPageLocators.user_link)
        # Check manage user link exist
        assert user_link.is_displayed()
        try:
            company_link = self.driver.find_elements(*RealmaxMainPageLocators.company_link)
        except NoSuchElementException:
            pass
        # Check manage company not exist
        if len(company_link) > 0:
            assert False
        
        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        self.driver.get("https://www.realmax.ga/logout")
        login_page.login('root', 'abc123')
        dashboard_page.navigatetouserpage()
        time.sleep(10)
        user_page.deleteUser('sele@gmail.com')

    def tearDown(self):

        self.driver.close() 
    
class RootUserCreateUserAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
    
    def test(self):
        # Navigate to user manage page
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetouserpage()
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('sele','sele','Robotic','User','sele@gmail.com','Test@123','Test@123','0904536477')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))

        ######################
        #                    #
        ###   Checkpoint   ###
        #                    #
        ######################
        verify_sele_text = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'sele')]//td[contains(.,'User')]")
        # Check create user success
        assert verify_sele_text.is_displayed()
        self.driver.get(realmax_url + "\logout")
        login_page = loginpage.init(self.driver)
        login_page.login('sele@gmail.com', 'Test@123')
        time.sleep(2)
        try:
            admin_link = self.driver.find_elements(*RealmaxMainPageLocators.admin_link)
        except NoSuchElementException:
            pass
        # Check admin link not exist if exist return fail
        if len(admin_link) > 0:
            assert False
         
        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        self.driver.get(realmax_url + "logout")
        login_page.login('root', 'abc123')
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('sele@gmail.com')

    def tearDown(self):

        self.driver.close() 

class AdminUserCreateUserAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get("https://www.realmax.ga")
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
    
    def test(self):
        # Create admin user
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetouserpage()
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('seleadmin','sele','Robotic','Administrator','seleadmin@gmail.com','Test@123','Test@123','0904536477')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))

        # Create User user
        self.driver.get("https://www.realmax.ga/logout")
        login_page = loginpage.init(self.driver)
        login_page.login('seleadmin@gmail.com', 'Test@123')
        time.sleep(5)
        admin_link = self.driver.find_element(*RealmaxMainPageLocators.admin_link)
        admin_link.click()
        dashboard_page.navigatetouserpage()
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('seleuser','sele','Robotic','User','seleuser@gmail.com','Test@123','Test@123','0904536477')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))

        ######################
        #                    #
        ###   Checkpoint   ###
        #                    #
        ######################
        verify_sele_text = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'seleuser')]//td[contains(.,'User')]")
        # Check create user success
        assert verify_sele_text.is_displayed()
        self.driver.get("https://www.realmax.ga/logout")
        login_page.login('seleuser@gmail.com', 'Test@123')
        time.sleep(2)
        try:
            admin_link = self.driver.find_elements(*RealmaxMainPageLocators.admin_link)
        except NoSuchElementException:
            pass
        # Check admin link not exist if exist return fail
        if len(admin_link) > 0:
            assert False

        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        self.driver.get("https://www.realmax.ga/logout")
        login_page.login('root', 'abc123')
        time.sleep(5)
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin@gmail.com')
        time.sleep(2)
        user_page.deleteUser('seleuser@gmail.com')

    def tearDown(self):

        self.driver.close() 