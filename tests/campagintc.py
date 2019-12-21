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
#setting
from config.setting import *

class Campaign(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)
    
    #@unittest.skip("demonstrating skipping")
    def test_1_Create_New_Campaign(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)

        ## Add new campaign
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToCampaignPage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        campaign_page = campaignpage.init(self.driver)
        users = ['seleuser']
        campaign_page.addNewCampaign('sele test campaign', ['Realmax', 'blacklist', 'free member'], users)

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        # Check sele campaign in campaign list
        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        time.sleep(5)
        try:
            sele_test_campaign = self.driver.find_elements(By.XPATH,".//div[@class='main-content']//div[@id='table_data_wrapper']//div[@class='row' and contains(.,'sele test campaign')]//table[@id='table_data']//td[contains(.,'sele test campaign')]")
        except NoSuchElementException:
            pass
        if len(sele_test_campaign) > 0:
            print "Checkpoint1[Pass]: Sele campaign display"
            assert True
        else:
            print "Checkpoint1[Failed]: Sele campaign not displayed"
            exitflag = 1    
        self.driver.close() 

        if exitflag == 1:
            assert False

    #@unittest.skip("demonstrating skipping")
    def test_2_User_Access_To_Campaign(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_user, gb_user_pass)

        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToCampaignPage()

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        time.sleep(5)
        try:
            sele_test_campaign = self.driver.find_elements(By.XPATH,".//div[@class='main-content']//div[@id='table_data_wrapper']//div[@class='row' and contains(.,'sele test campaign')]//table[@id='table_data']//td[contains(.,'sele test campaign')]")
        except NoSuchElementException:
            pass
        if len(sele_test_campaign) > 0:
            print "Checkpoint1[Pass]: Sele campaign displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Sele campaign not displayed"
            exitflag = 1   
        self.driver.close()

        if exitflag == 1:
            assert False

    #@unittest.skip("demonstrating skipping")
    def test_3_User_Cannot_Create_or_Edit_Campaign(self):
        exitflag = 0
        login_page = loginpage.init(self.driver)
        login_page.login(gb_user, gb_user_pass)
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToCampaignPage()

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        time.sleep(5)
        try:
            new_campaign_button = self.driver.find_elements(By.XPATH, ".//div[@class='container-fluid']//div[@class='page-header']//span[contains(.,'New campaign')]")
        except NoSuchElementException:
            pass
        if len(new_campaign_button) == 0:
            assert True
            print "Checkpoint1[Pass]: Create new campaign button not display "
        else:
            print "Checkpoint1[Failed]: Create new campaign button displayed"
            exitflag = 1

        try:
            new_campaign_link = self.driver.find_elements(By.XPATH, ".//ul[@class='nav']//li[@title='new-campaign']")
        except NoSuchElementException:
            pass
        if len(new_campaign_link) == 0:
            assert True
            print "Checkpoint2[Pass]: Create new campaign link not display "
        else:
            print "Checkpoint2[Failed]: Create new campaign link displayed "
            exitflag = 1

        try:
            edit_campaign_icon = self.driver.find_elements(By.XPATH, ".//table[@id='table_data']//tr[contains(.,'sele test campaign')]//div[@name='sele test campaign']//span[@title='Edit']")
        except NoSuchElementException:
            pass
        if len(edit_campaign_icon) == 0:
            assert True
            print "Checkpoint3[Pass]: Edit campaign icon not display "
        else:
            print "Checkpoint3[Failed]: Edit campaign icon displayed "
            exitflag = 1

        self.driver.close()
        
        if exitflag == 1:
            assert False

    def test_4_Edit_Campain(self):
        login_page = loginpage.init(self.driver)
        login_page.login(gb_admin, gb_admin_pass)
        dashboard_page = dashboardpage.init(self.driver)
        dashboard_page.navigateToCampaignPage()

        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        campaign_page = campaignpage.init(self.driver)
        campaign_page.editCampaign('sele test campaign', 'sele test campaign2', ['Realmax'])

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        exitflag = 0
        # Check sele campaign 2 in campaign list
        WebDriverWait(self.driver,10).until(cond.title_is("Manage campaign"))
        time.sleep(5)
        try:
            sele_test_campaign2 = self.driver.find_elements(By.XPATH,".//div[@class='main-content']//div[@id='table_data_wrapper']//div[@class='row' and contains(.,'sele test campaign2')]//table[@id='table_data']//td[contains(.,'sele test campaign2')]")
        except NoSuchElementException:
            pass
        if len(sele_test_campaign2) > 0:
            print "Checkpoint1[Pass]: Sele campaign 2 displayed"
            assert True
        else:
            print "Checkpoint1[Failed]: Sele campaign 2 not displayed"
            exitflag = 1

        try:
            user_list = Select(self.driver.find_element_by_xpath(".//select[@id='select-user']"))
        except NoSuchElementException:
            pass
        if user_list:
            user_list.select_by_visible_text('seleuser user')
        time.sleep(2)
        try:
            sele_test_campaign2 = self.driver.find_elements(By.XPATH,".//div[@class='main-content']//div[@id='table_data_wrapper']//div[@class='row' and contains(.,'sele test campaign2')]//table[@id='table_data']//td[contains(.,'sele test campaign2')]")
        except NoSuchElementException:
            pass
        if len(sele_test_campaign2) == 0:
            print "Checkpoint2[Pass]: Sele campaign 2 not displayed"
            assert True
        else:
            print "Checkpoint2[Failed]: Sele campaign 2 displayed"
            exitflag = 1
        
        self.driver.close()

        if exitflag == 1:
            assert False

        



class AddNewContactToCampagin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(gb_chromedriverlocation)
        self.driver.maximize_window()
        self.driver.get(realmax_url)

    def test(self):
        # Login to realmax
        login_page = loginpage.init(self.driver)
        # login_page.login('root', 'abc123')
        
        # # Add company
        dashboard_page = dashboardpage.init(self.driver)
        # dashboard_page.navigatetocompanypage()
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        company_page = companypage.init(self.driver)
        # company_page.addnewcompany('sele', 'selecompany', gb_access_token, gb_refesh_token)
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        # dashboard_link = self.driver.find_element(*RealmaxMainPageLocators.dashboard_link)
        # dashboard_link.click()
        # WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        # dashboard_page.navigatetouserpage()

        # # Add admin sele
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        # time.sleep(2)
        # user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        # user_btn.click()
        user_page = userpage.init(self.driver)
        # user_page.addNewUser('sele','admin','selecompany','Administrator','seleadmin@gmail.com','Test@123','Test@123','0904536477')

        # # Add user sele
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        # time.sleep(2)
        # user_btn = self.driver.find_element(*RealmaxUserPageLocators.addnew_user_btn)
        # user_btn.click()
        # user_page.addNewUser('sele','user','selecompany','User','seleuser@gmail.com','Test@123','Test@123','0904536477')

        # Login to admin sele
        self.driver.get(realmax_url + "/logout")
        login_page.login('seleadmin@gmail.com', 'Test@123')
        WebDriverWait(self.driver,10).until(cond.title_is("Dashboard"))
        
        #Set display support field
        dashboard_page.navigateToMyCompanyPage()
        time.sleep(5)
        user_support_chbox = self.driver.find_element_by_xpath(".//input[@id='custom-field-44']")
        user_support_chbox.click()
        save_btn = self.driver.find_element(*RealmaxCompanyPageLocators.save_btn)
        save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()

        #Add new SeleCampaign
        dashboard_page.navigateToCampaignPage()
        time.sleep(5)
        new_campaign_link = self.driver.find_element(*RealmaxCampaignPageLocators.add_new_campaign_btn)
        new_campaign_link.click()
        tags = ['[VIP]', '[Potential]', '[Standard]']
        users = ['sele user']
        campaign_page = campaignpage.init(self.driver)
        campaign_page.addNewCampaign('selecampain', tags, users)
        time.sleep(3)

        # Add [Vip] tag to user sele
        dashboard_page.navigatetouserpage()
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        user_page.appplyTagToUser('seleuser@gmail.com', '[Vip]')

        # Add new contact apply tag
        time.sleep(2)
        dashboard_page.navigateToAddContactPage()
        time.sleep(2)
        contact_page = contactpage.init(self.driver)
        contact_page.addnewcontact('sele', 'contact', 'selecontact@gmail.com', 'sele - seleuser@gmail.com')
        contact_page.applyTagToContact('selecontact@gmail.com', '[Vip]')

        ######################
        #                    #
        #    Checkpoint      #
        #                    #
        ######################
        # Check selecontact in campaign
        dashboard_page.navigateToCampaignPage()
        add_contact_link = self.driver.find_element_by_xpath("")
        # try:
        #     pages = self.driver.find_element_by_xpath(".//ul[@class='pagination']//li[@class='paginate_button ']")
        # except NoSuchElementException:
        #     pass
        # if len(pages) > 0:
        #     i = 2
        #     while i < len(pages) + 2:
        #         try:
        #             selecampaign_addcontact = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(., 'selecampaign'//span[@title='Contact management'])]")
        #             selecampaign_addcontact.click()
                    

    def tearDown(self):
        self.driver.close() 