from locator.locators import RealmaxMainPageLocators
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#setting
from config.setting import *

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def navigatetocompanypage(self):
        try:
            side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        except NoSuchElementException:
            pass
        if len(side_menu_close_link) > 0:
            pass
        else:
            side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
            side_menu_open_link.click()
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")))
        admin_link = self.driver.find_element(*RealmaxMainPageLocators.admin_link)
        admin_link.click()
        time.sleep(2)
        company_link = self.driver.find_element(*RealmaxMainPageLocators.company_link)
        company_link.click()

    def navigatetouserpage(self):
        # try:
        #     side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        # except NoSuchElementException:
        #     pass
        # if len(side_menu_close_link) > 0:
        #     pass
        # else:
        #     side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
        #     side_menu_open_link.click()
        # WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")))
        # time.sleep(2)
        # admin_link = self.driver.find_element(*RealmaxMainPageLocators.admin_link)
        # admin_link.click()
        # time.sleep(2)
        # # handle cant click user link
        # action = ActionChains(self.driver)
        # admin_link = self.driver.find_element(*RealmaxMainPageLocators.admin_link)
        # action.move_to_element(admin_link).perform()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # user_link = self.driver.find_element(*RealmaxMainPageLocators.user_link)
        # user_link.click()
        self.driver.get(realmax_url + '/admin/user/list')

    def navigateToAddContactPage(self):
        try:
            side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        except NoSuchElementException:
            pass
        if len(side_menu_close_link) > 0:
            pass
        else:
            side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
            side_menu_open_link.click()
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")))
        contact_link = self.driver.find_element(*RealmaxMainPageLocators.contact_link)
        contact_link.click()
        time.sleep(2)
        newcontact_link = self.driver.find_element(*RealmaxMainPageLocators.new_contact_link)
        newcontact_link.click()

    def navigateToTagPage(self):
        # try:
        #     side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        # except NoSuchElementException:
        #     pass
        # if len(side_menu_close_link) > 0:
        #     pass
        # else:
        #     side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
        #     side_menu_open_link.click()
        # tag_link = self.driver.find_element(*RealmaxMainPageLocators.tag_link)
        # tag_link.click()
        # WebDriverWait(self.driver,10).until(cond.title_is("Manage tag"))
        self.driver.get(realmax_url + '/tag/list')


    def navigateToManageContactPage(self):
        # try:
        #     side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        # except NoSuchElementException:
        #     pass
        # if len(side_menu_close_link) > 0:
        #     pass
        # else:
        #     side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
        #     side_menu_open_link.click()
        # WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")))
        # time.sleep(5)
        # contact_link = self.driver.find_element(*RealmaxMainPageLocators.contact_link)
        # contact_link.click()
        # time.sleep(2)
        # manage_contact_link = self.driver.find_element(*RealmaxMainPageLocators.manage_contact_link)
        # manage_contact_link.click()
        self.driver.get(realmax_url + '/contact/list')
        

    def navigateToCampaignPage(self):
        try:
            side_menu_close_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_close_link)
        except NoSuchElementException:
            pass
        if len(side_menu_close_link) > 0:
            pass
        else:
            side_menu_open_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_open_link)
            side_menu_open_link.click()
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")))
        time.sleep(5)
        campaign_link = self.driver.find_element(*RealmaxMainPageLocators.campaign_link)
        campaign_link.click()
        time.sleep(2)
        manage_campaign_link = self.driver.find_element(*RealmaxMainPageLocators.manage_campaign_link)
        manage_campaign_link.click()

    def navigateToMyCompanyPage(self):
        admin_profile_link = self.driver.find_element(*RealmaxMainPageLocators.admin_profile_link)
        admin_profile_link.click()
        time.sleep(1)
        admin_mycompany_link = self.driver.find_element(*RealmaxMainPageLocators.admin_mycompany_link)
        admin_mycompany_link.click()

    def navigateToMyProfilePage(self):
        admin_profile_link = self.driver.find_element(*RealmaxMainPageLocators.admin_profile_link)
        admin_profile_link.click()
        time.sleep(1)
        admin_myprofile_link = self.driver.find_element(*RealmaxMainPageLocators.admin_myprofile_link)
        admin_myprofile_link.click()

