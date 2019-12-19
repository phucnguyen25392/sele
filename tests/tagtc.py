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
#setting
from config.setting import *

class AdminSetTagToContact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test(self):
        # Login to realmax
        login_page = loginpage.init(self.driver)
        login_page.login('root', 'abc123')
        
        # Add company
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigatetocompanypage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        company_page = companypage.init(self.driver)
        company_page.addnewcompany('sele', 'selecompany', gb_access_token, gb_refesh_token)
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        dashboard_link = self.driver.find_element(*RealmaxMainPageLocators.dashboard_link)
        dashboard_link.click()
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()

        # Add admin sele
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page = userpage.init(self.driver)
        user_page.addNewUser('sele','admin','selecompany','Administrator','seleadmin@gmail.com','Test@123','Test@123','0904536477')

        # Add user sele
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        user_btn.click()
        user_page.addNewUser('sele','user','selecompany','User','seleuser@gmail.com','Test@123','Test@123','0904536477')

        # Login to admin sele
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        dashboard_page.navigatetouserpage()

        # Add [Vip] tag to user sele
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page.appplyTagToUser('seleuser@gmail.com', '[Vip]')
        
        # Add new contact apply tag
        time.sleep(2)
        dashboard_page.navigateToAddContactPage()
        time.sleep(2)
        contact_page = contactpage.init(self.driver)
        contact_page.addnewcontact('sele', 'contact', 'selecontact@gmail.com')
        contact_page.applyTagToContact('selecontact@gmail.com', '[Vip]')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        time.sleep(5)
        dashboard_page.navigateToTagPage()
        time.sleep(5)
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i < len(pages) + 2:
                try:
                    vip_tag = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'[VIP]')]")
                except NoSuchElementException:
                    pass
                if len(vip_tag) == 0:
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(5)
                    i += 1
                else:
                    break
        tag_page = tagpage.init(self.driver)
        tag_page.removeContagInTag('[VIP]', 'Sele')
        dashboard_page.navigateToManageContactPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        time.sleep(5)
        # Check [VIP] tag is removed in contact
        add_tag_link = self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'selecontact@gmail.com')]//span[@title='Apply tags to this contact']")
        add_tag_link.click()
        try:
            verify_vip_tag = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//label[contains(., '[VIP]')]")
        except NoSuchElementException:
            pass
        if len(verify_vip_tag) > 0:
            assert False
        time.sleep(3)
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
        contact_page.removeContact('selecontact@gmail.com')
        time.sleep(2)
        self.driver.get("https://www.realmax.ga/logout")
        login_page.login('root', 'abc123')
        time.sleep(5)
        dashboard_page.navigatetouserpage()
        user_page.deleteUser('seleadmin@gmail.com')
        time.sleep(2)
        dashboard_page.navigatetocompanypage()
        company_page.deletecompany('sele')



    def tearDown(self):
        self.driver.close() 

