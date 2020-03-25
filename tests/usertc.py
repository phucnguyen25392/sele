import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# Page 
import pageobject.loginpage as loginpage
import pageobject.dashboardpage as dashboardpage
import pageobject.companypage as companypage
import pageobject.userpage as userpage
import pageobject.contactpage as contactpage
import pageobject.profilepage as profilepage
import pageobject.tagpage as tagpage
# Locator
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxMainPageLocators

#setting
from config.setting import *

class User(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    #@unittest.skip("demonstrating skipping")
    def test_1_Change_Info_In_My_Profile(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        profile_page = profilepage.init(self.driver)

        # Create new user 'seleuser2'
        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','Realmax','User','phucnguyen25392+seleuser2@gmail.com','Test@123','Test@123','0904536477')
        self.driver.get(realmax_url + "/logout")

        # Login to user
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        dashboard_page.navigateToMyProfilePage()
        profile_page.edituserinfo('test','Change_Info_In_My_Profile', 'Test@123','Test@1234')
        WebDriverWait(self.driver,10).until(cond.title_is("User"))
        time.sleep(2)
        dashboard_page.navigateToManageContactPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@1234')

        try:
            text_change_info = self.driver.find_elements(By.XPATH,".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a[@class='dropdown-toggle']//span[contains(.,'test Change_Info_In_My_Profile')]")
        except NoSuchElementException:
            pass
        if len(text_change_info) > 0:
            print "Checkpoint1[Pass]: Login success 'test Change_Info_In_My_Profile' displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Login not success 'test Change_Info_In_My_Profile' not displayed"
            exitflag = 1
        
        self.driver.quit()

        if exitflag == 1:
            assert False
    
    #@unittest.skip("demonstrating skipping")
    def test_2_Admin_Edit_Exist_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        profile_page = profilepage.init(self.driver)

        # Login to user
        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page.navigatetouserpage()
        user_page.editUser('phucnguyen25392+seleuser2@gmail.com', 'sele', 'user2', 'Test@123')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        exitflag_cp1 = 0
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    sele2_user = self.driver.find_elements_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'sele') and contains(., 'user2')]")
                except NoSuchElementException:
                    pass
                if len(sele2_user) == 0:
                    time.sleep(2)
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(3)
                    i += 1
                    exitflag_cp1 = 1
                else:
                    exitflag_cp1 = 0
                    break
        if exitflag_cp1 == 0:
            print "Checkpoint1[Pass]: Sele user2 displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Sele user2 not displayed"
            exitflag = 1

        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')

        try:
            text_change_info = self.driver.find_elements(By.XPATH,".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown']/a[@class='dropdown-toggle']//span[contains(.,'sele user2')]")
        except NoSuchElementException:
            pass
        if len(text_change_info) > 0:
            print "Checkpoint2[Pass]: Login success 'sele user2' displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Login not success 'tsele user2' not displayed"
            exitflag = 1
            
        self.driver.close()
        if exitflag == 1:
            assert False

    #@unittest.skip("demonstrating skipping")
    def test_3_User_Cannot_Delete_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        profile_page = profilepage.init(self.driver)

        # Login to user
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        dashboard_page.navigatetouserpage()
        time.sleep(3)    
        url = self.driver.current_url

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        if url == 'https://app.realcrm.vn/403':
            print "Checkpoint1[Pass]: User cannot navigate to user manage page"
            assert True
        else:
            print "Checkpoint1[Failed]: User can navigate to user manage page"
            exitflag = 1

        self.driver.quit()

        if exitflag == 1:
            assert False

    #@unittest.skip("demonstrating skipping")
    def test_4_Grant_Tag_Permission_To_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        profile_page = profilepage.init(self.driver)
        tag_page = tagpage.init(self.driver)
        wait = WebDriverWait(self.driver, 10)

        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page.appplyTagToUser('phucnguyen25392+seleuser2@gmail.com','Realmax')

        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        dashboard_page.navigateToTagPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage tag"))

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, ".//table[@id='table_data']//tr[contains(.,'Realmax')]//td[contains(.,'Realmax')]")))
            realmax_tag = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'Realmax')]//td[contains(.,'Realmax')]")
        except NoSuchElementException:
            pass
        if len(realmax_tag) > 0:
            print "Checkpoint1[Pass]: Realmax tag displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Realmax tag not displayed"
            exitflag = 1

        self.driver.quit()

        if exitflag == 1:
            assert False

    def test_5_Delete_A_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        profile_page = profilepage.init(self.driver)
        tag_page = tagpage.init(self.driver)
        wait = WebDriverWait(self.driver, 10)

        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page.deleteUser('phucnguyen25392+seleuser2@gmail.com')
        time.sleep(10)
        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    sele_user = self.driver.find_elements_by_xpath(".//table[@id='table_data']//tr[contains(.,'phucnguyen25392+seleuser2@gmail.com')]//td[contains(.,'phucnguyen25392+seleuser2@gmail.com')]")
                except NoSuchElementException:
                    pass
                if len(sele_user) > 0:
                    exitflag = 1
                    break
                else:
                    if i == len(pages) + 2:
                        break
                    else:    
                        time.sleep(2)
                        page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                        page_navigate_btn.click()
                        time.sleep(3)
                        i += 1

        if exitflag == 0:
            print "Checkpoint1[Pass]: User sele2 deleted successfully"
            assert True
        else:
            print "Checkpoint1[Failed]: User sele2 not deleted successfully"
            exitflag = 1

        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # dashboard_page.navigateToManageContactPage()
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        # time.sleep(10)
        # contact_page.removeContact('phucnguyen25392+seleuser2@gmail.com')

        self.driver.quit()
        if exitflag == 1:
            assert False

        

        
    
    