import unittest
import time
import datetime
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
import pageobject.userpage as userpage
import pageobject.contactpage as contactpage
# Locator
from locator.locators import RealmaxCompanyPageLocators
from locator.locators import RealmaxMainPageLocators
from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxContactPageLocators
#setting
from config.setting import *
from config.bcolors import *
# Element
import element.element as element

class Notification(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    #@unittest.skip("demonstrating skipping")   
    def test_1_SendNoti_When_Delete_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        checkElement = element.init(self.driver)

        # Login to realmax
        login_page.login(gb_admin, gb_admin_pass)

        # Add adminsele2
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','admin2','Realmax','Administrator','phucnguyen25392+seleadmin2@gmail.com','Test@123','Test@123','0904536477')

        # Add usersele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','Realmax','User','phucnguyen25392+seleuser2@gmail.com','Test@123','Test@123','0904536477')
        self.driver.get(realmax_url + "/logout")

        # Delete usersele2
        login_page.login(gb_admin, gb_admin_pass)
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('phucnguyen25392+seleuser2@gmail.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        #Check noti in seleadmin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            sele_delete_noti = self.driver.find_elements(By.XPATH,".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'phucnguyen25392+seleuser2@gmail.com') and contains(.,'was deleted by phucnguyen25392+seleadmin@gmail.com') and contains(.,'less than a minute ago')]")
        except NoSuchElementException:
            pass
        if len(sele_delete_noti) > 0:
            print "Checkpoint1[Pass]: Delete seleuser notification displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Delete seleuser notification not displayed"
            exitflag = 1    

        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # Delete seleadmin2 seleuser2 contact
        # self.driver.get(realmax_url + "/logout")
        # login_page.login(gb_admin, gb_admin_pass)
        # WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        # dashboard_page.navigateToManageContactPage()
        # contact_page.removeContact('phucnguyen25392+seleadmin2@gmail.com')
        # time.sleep(3)
        # contact_page.removeContact('phucnguyen25392+seleuser2@gmail.com')

        if exitflag == 1:
            assert False
        self.driver.close()

    #@unittest.skip("demonstrating skipping")
    def test_3_SendNoti_When_Mess_To_Specific_User(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        
        # Login to realmax
        login_page.login(gb_admin, gb_admin_pass)
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        # Add user sele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','Realmax','User','phucnguyen25392+seleuser2@gmail.com','Test@123','Test@123','0904536477')

        # Add user sele3
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user3','Realmax','User','phucnguyen25392+seleuser3@gmail.com','Test@123','Test@123','0904536477')

        # Send message to specific users
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        dashboard_page.navigatetouserpage()
        names = ['sele admin2', 'sele user2']
        now = datetime.datetime.now()
        mess = now.strftime("%H:%M:%S")
        time.sleep(2)
        user_page.sendMessageToUsers( mess, 'https://www.google.com', names)

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        # Check mess admin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            print "Checkpoint1[Pass]: Message" + mess +  "displayed in seleadmin account"
            assert True
        else:
            print "Checkpoint1[Failed]: Message" + mess +  "not displayed in seleadmin account"
            exitflag = 1    
            

        # Check mess user2
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            print "Checkpoint2[Pass]: Message" + mess +  "displayed in seleuser account"
            assert True
        else:
            print "Checkpoint2[Failed]: Message" + mess +  "not displayed in seleuser account"
            exitflag = 1   
            

        # Check mess user3
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser3@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            assert True
        if len(verify) == 0:
            print "Checkpoint3[Pass]: Message" + mess +  " not displayed in seleuser account"
            assert True
        else:
            print "Checkpoint3[Failed]: Message" + mess +  "displayed in seleuser account"
            exitflag = 1  

        if exitflag == 1:
            assert False
        self.driver.close()


    #@unittest.skip("demonstrating skipping")
    def test_4_SendNotiWhenMessAllUser_AsAdmin(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)

        # Send message to all users
        login_page.login(gb_admin, gb_admin_pass)
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        now = datetime.datetime.now()
        mess = now.strftime("%H:%M:%S")
        user_page.sendMessageToUsers( mess, 'https://www.google.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        # Check mess admin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            print "Checkpoint1[Pass]: Message" + mess +  "displayed in seleadmin account"
            assert True
        else:
            print "Checkpoint1[Failed]: Message" + mess +  "not displayed in seleadmin account"
            exitflag = 1 
            

        # Check mess user2
        self.driver.get(realmax_url + "/logout")
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            print "Checkpoint2[Pass]: Message" + mess +  "displayed in seleuser account"
            assert True
        else:
            print "Checkpoint2[Failed]: Message" + mess +  "not displayed in seleuser account"
            exitflag = 1 

        if exitflag == 1:
            assert False
        self.driver.close()  

    #@unittest.skip("demonstrating skipping")
    def test_5_SendNotiWhenMessAllUser_AsUser(self):

        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        
        # Checkmessage button 
        login_page.login('phucnguyen25392+seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        try:
            verify = self.driver.find_elements(By.XPATH, ".//div[@id='btn-new-message']")
        except NoSuchElementException:
            pass
        if len(verify) == 0:
            print "Checkpoint1[Pass]: New message button not displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: New message button displayed"
            exitflag = 1 
    
        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # Delete seleadmin2, seleuser2, seleuser3
        self.driver.get(realmax_url + "/logout")
        login_page.login(gb_admin, gb_admin_pass)
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page.deleteUser('phucnguyen25392+seleadmin2@gmail.com')
        time.sleep(2)
        user_page.deleteUser('phucnguyen25392+seleuser2@gmail.com')
        time.sleep(2)
        user_page.deleteUser('phucnguyen25392+seleuser3@gmail.com')
        time.sleep(5)

        # Delete seleadmin2 seleuser2 contact
        # dashboard_page.navigateToManageContactPage()
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        # time.sleep(3)
        # contact_page.removeContact('phucnguyen25392+seleuser2@gmail.com')
        # time.sleep(3)
        # contact_page.removeContact('phucnguyen25392+seleuser3@gmail.com')

        if exitflag == 1:
            assert False
        self.driver.close()



