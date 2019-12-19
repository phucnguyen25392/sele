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
import pageobject.userpage as userpage
# Locator
from locator.locators import RealmaxCompanyPageLocators
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxMainPageLocators
#setting
from config.setting import *


class RootInsertValidToken(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.get("https://www.realmax.ga")

    def test(self):
        
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
        
        # Navigate to company page
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetocompanypage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        company_page = companypage.init(self.driver)
        company_page.addnewcompany('sele', 'test', gb_access_token, gb_refesh_token)
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        verify_sele_text = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'sele')]//td[contains(.,'VERIFIED')]")
        # Check "Verify" text is shown in sele company info line
        assert verify_sele_text.is_displayed()
        edit_sele_link =  self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'sele')]//span[@title='Edit']")
        edit_sele_link.click()
        WebDriverWait(self.driver,10).until(cond.title_is("Company"))
        checktoken_btn = self.driver.find_element_by_xpath("//*[@id='btn-check-infusion-auth']")
        checktoken_btn.click()
        time.sleep(5)
        token_success_message = self.driver.find_element(*RealmaxCompanyPageLocators.token_success_message)
        # Check Verify message appear when click in verify in sele company
        assert token_success_message.is_displayed()
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()

        ######################
        #                    #
        #    Clean up        #
        #                    #
        ###################### 
        time.sleep(2)
        save_btn = self.driver.find_element(*RealmaxCompanyPageLocators.save_btn)
        save_btn.click()
        time.sleep(5)
        ok_btn.click()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        time.sleep(5)
        del_sele_link =  self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'sele')]//span[@title='Remove']")
        del_sele_link.click()
        time.sleep(2)
        confirm_delete_ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.confirm_delete_ok_btn)
        confirm_delete_ok_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()

    def tearDown(self):
        self.driver.close() 

class RootInsertInvalidToken(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.get("https://www.realmax.ga")

    def test(self):
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
        
        # Navigate to company page
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetocompanypage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        company_page = companypage.init(self.driver)
        company_page.addnewcompany('sele', 'test', '123', '123')
        checktoken_btn = self.driver.find_element(*RealmaxCompanyPageLocators.checktoken_btn)
        checktoken_btn.click()
        time.sleep(2)

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################

        token_invalid_message = self.driver.find_element(*RealmaxCompanyPageLocators.token_invalid_message)
        assert token_invalid_message.is_displayed()

    def tearDown(self):
        self.driver.close()

class AdminInsertValidToken(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get("https://www.realmax.ga")

    def test(self):
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
        # Create a test company
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetocompanypage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        company_page = companypage.init(self.driver)
        company_page.addnewcompany('selecompany', 'Selecompany')
        self.driver.get("https://www.realmax.ga")

        # Create admin user
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetouserpage()
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('seleadmin','sele','Selecompany','Administrator','seleadmin@gmail.com','Test@123','Test@123','0904536477')
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))

        # Add valid token with admin
        self.driver.get("https://www.realmax.ga/logout")
        login_page = loginpage.init(self.driver)
        login_page.login('seleadmin@gmail.com', 'Test@123')
        userprofile_link = self.driver.find_element(*RealmaxMainPageLocators.userprofile_link)
        userprofile_link.click()
        mycompany_link = self.driver.find_element(*RealmaxMainPageLocators.mycompany_link)
        mycompany_link.click()
        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        access_token_tb = self.driver.find_element(*RealmaxCompanyPageLocators.accesstoken_tb)
        access_token_tb.send_keys(gb_access_token)
        refesh_token_tb = self.driver.find_element(*RealmaxCompanyPageLocators.refresh_tb)
        refesh_token_tb.send_keys(gb_refesh_token)
        checktoken_btn = self.driver.find_element(*RealmaxCompanyPageLocators.checktoken_btn)
        checktoken_btn.click()
        time.sleep(5)
        token_success_message = self.driver.find_element(*RealmaxCompanyPageLocators.token_success_message)
        # Check Verify message appear when click in verify in sele company
        assert token_success_message.is_displayed()
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()
        ######################
        #                    #
        #    Clean up        #
        #                    #
        ###################### 
        self.driver.get("https://www.realmax.ga/logout")
        login_page.login('root', 'abc123')
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin@gmail.com')
        self.driver.get("https://www.realmax.ga")
        dashboard_page.navigatetocompanypage()
        company_page.deletecompany('selecompany')
        
        
    def tearDown(self):
        self.driver.close()


    