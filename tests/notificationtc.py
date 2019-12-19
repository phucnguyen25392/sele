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

class SendNotiWhenDeleteUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)
        
    def test(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        checkElement = element.init(self.driver)

        # Login to realmax
        login_page.login('root', 'abc123')

        # Add adminsele2
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','admin2','RealPlus','Administrator','seleadmin2@gmail.com','Test@123','Test@123','0904536477')

        # Add usersele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','RealPlus','User','seleuser2@gmail.com','Test@123','Test@123','0904536477')
        self.driver.get(realmax_url + "/logout")

        # Delete usersele2
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleuser2@gmail.com')

        #Check noti in seleadmin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################

        self.assertTrue(checkElement.is_element_present(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'seleuser2@gmail.com') and contains(.,'was deleted by seleadmim@gmail.com') and contains(.,'less than a minute ago')]"))
        
        
        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # Delete seleadmin2, seleuser2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin2@gmail.com')

        # Delete seleadmin2 seleuser2 contact
        dashboard_page.navigateToManageContactPage()
        contact_page.removeContact('seleadmin2@gmail.com')
        time.sleep(3)
        contact_page.removeContact('seleuser2@gmail.com')

    def tearDown(self):
        self.driver.close() 

class SendNotiWhenMessSpecUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        
        # Login to realmax
        login_page.login('root', 'abc123')

        # Add admin sele2
        time.sleep(2)
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','admin2','RealPlus','Administrator','seleadmin2@gmail.com','Test@123','Test@123','0904536477')

        # Add user sele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','RealPlus','User','seleuser2@gmail.com','Test@123','Test@123','0904536477')

        # Add user sele3
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user3','RealPlus','User','seleuser3@gmail.com','Test@123','Test@123','0904536477')

        self.driver.get(realmax_url + "/logout")

        # Send message to specific users
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
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

        # Check mess admin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            assert True
        if len(verify) > 0:
            assert True
            print "Checkpoint1: Message " + mess + " display correctly"
        else:
            print "Checkpoint1: Message " + mess + " display incorrectly"
            assert False
            

        # Check mess user2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            assert True
        if len(verify) > 0:
            assert True
            print "Checkpoint2: Message " + mess + " display correctly"
        else:
            print "Checkpoint2: Message " + mess + " display incorrectly"
            assert False
            

        # Check mess user3
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleuser3@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            assert True
        if len(verify) > 0:
            print "Checkpoint3: Message " + mess + " display incorrectly"
            assert False
        else:
            assert True
            print "Checkpoint3: Message " + mess + " display correctly"

        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # Delete seleadmin2, seleuser2, seleuser3
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin2@gmail.com')
        time.sleep(2)
        user_page.deleteUser('seleuser2@gmail.com')
        time.sleep(2)
        user_page.deleteUser('seleuser3@gmail.com')

        # Delete seleadmin2 seleuser2 contact
        dashboard_page.navigateToManageContactPage()
        contact_page.removeContact('seleadmin2@gmail.com')
        time.sleep(3)
        contact_page.removeContact('seleuser2@gmail.com')
        time.sleep(3)
        contact_page.removeContact('seleuser3@gmail.com')

    def tearDown(self):
        self.driver.close()

class SendNotiWhenMessAllUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test_AsAdmin(self):
        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)
        
        # Login to realmax
        login_page.login('root', 'abc123')
    
        dashboard_page.navigatetouserpage()

        # Add admin sele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','admin2','RealPlus','Administrator','seleadmin2@gmail.com','Test@123','Test@123','0904536477')

        # Add user sele2
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user2','RealPlus','User','seleuser2@gmail.com','Test@123','Test@123','0904536477')

        self.driver.get(realmax_url + "/logout")

        # Send message to specific users
        login_page.login('seleadmim@gmail.com', 'Test@123')
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

        # Check mess admin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            assert True
            print "Checkpoint1: Message " + mess + " display correctly"
        else:
            print "Checkpoint1: Message " + mess + " display incorrectly"
            assert False
            

        # Check mess user2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            assert True
            print "Checkpoint2: Message " + mess + " display correctly"
        else:
            print "Checkpoint2: Message " + mess + " display incorrectly"
            assert False
            

    def test_AsUser(self):

        # INIT
        login_page = loginpage.init(self.driver)
        dashboard_page = dashboardpage.init(self.driver)
        user_page = userpage.init(self.driver)
        contact_page = contactpage.init(self.driver)

        self.driver.get(realmax_url + "/logout")
        
        # Send message to specific users 
        login_page.login('seleuser2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        now = datetime.datetime.now()
        mess = now.strftime("%H:%M:%S")
        user_page.sendMessageToUsers( mess, 'https://www.google.com')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################

        # Check mess admin2
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin2@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            assert True
            print "Checkpoint1: Message " + mess + " display correctly"
        else:
            print "Checkpoint1: Message " + mess + " display incorrectly"
            assert False
            

        # Check mess admim
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        noti_link = self.driver.find_element(*RealmaxMainPageLocators.noti_link)
        noti_link.click()
        time.sleep(5)
        try:
            verify = self.driver.find_elements(By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif open']/ul[@class='dropdown-menu notifications']//li[@class='notif-items']//li[contains(.,'" + mess + "')]")
        except NoSuchElementException:
            pass
        if len(verify) > 0:
            assert True
            print "Checkpoint2: Message " + mess + " display correctly"
        else:
            print "Checkpoint2: Message " + mess + " display incorrectly"
            assert False
    
        ######################
        #                    #
        ###### Clean up ######
        #                    #
        ###################### 
        # Delete seleadmin2, seleuser2, seleuser3
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmim@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin2@gmail.com')
        time.sleep(2)
        user_page.deleteUser('seleuser2@gmail.com')

        # Delete seleadmin2 seleuser2 contact
        dashboard_page.navigateToManageContactPage()
        contact_page.removeContact('seleadmin2@gmail.com')
        time.sleep(3)
        contact_page.removeContact('seleuser2@gmail.com')

    def tearDown(self):
        self.driver.close()



