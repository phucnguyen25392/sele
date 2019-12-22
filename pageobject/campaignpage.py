from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locator.locators import RealmaxCampaignPageLocators
from selenium.common.exceptions import NoSuchElementException
import common.actions as actions
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def addNewCampaign(self, name, tags, users):
        time.sleep(2)
        try:
            add_new_campaign_btn = self.driver.find_element(*RealmaxCampaignPageLocators.add_new_campaign_btn)
        except NoSuchElementException:
            pass
        if add_new_campaign_btn:
            add_new_campaign_btn.click()
        WebDriverWait(self.driver,10).until(cond.title_is("Campaign"))
        name_tb = self.driver.find_element(*RealmaxCampaignPageLocators.name_tb)
        name_tb.send_keys(name)
        tag_tb = self.driver.find_element(*RealmaxCampaignPageLocators.tag_tb)
        for tag in tags:
            tag_tb.send_keys(tag)
            time.sleep(3)
            tag_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-tagsautocomplete-list']")
            tag_auto_complete.click()
            tag_tb.clear()
        user_tb = self.driver.find_element(*RealmaxCampaignPageLocators.user_tb)
        for user in users:
            user_tb.send_keys(user)
            time.sleep(3)
            user_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-usersautocomplete-list']")
            user_auto_complete.click()
            user_tb.clear()
        add_campaign_save_btn = self.driver.find_element(*RealmaxCampaignPageLocators.add_campaign_save_btn)
        add_campaign_save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.ok_btn)
        ok_btn.click()

    def editCampaign(self, name, new_name, tags,users=None):
        action = actions.init(self.driver)
        action.click('campaign','edit', name)
        WebDriverWait(self.driver,10).until(cond.title_is("Campaign"))
        name_tb = self.driver.find_element(*RealmaxCampaignPageLocators.name_tb)
        name_tb.clear()
        name_tb.send_keys(new_name)
        tag_tb = self.driver.find_element(*RealmaxCampaignPageLocators.tag_tb)
        # Cleaning up tags and users
        try:
            close_btns = self.driver.find_elements(By.XPATH, ".//span[@class='fa fa-close']")
        except NoSuchElementException:
            pass
        for close_btn in close_btns:
            close_btn.click()
            time.sleep(2)
        # Edit...
        for tag in tags:
            tag_tb.send_keys(tag)
            time.sleep(3)
            tag_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-tagsautocomplete-list']")
            tag_auto_complete.click()
            tag_tb.clear()
        user_tb = self.driver.find_element(*RealmaxCampaignPageLocators.user_tb)
        if users:
            for user in users:
                user_tb.send_keys(user)
                time.sleep(3)
                user_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-usersautocomplete-list']")
                user_auto_complete.click()
                user_tb.clear()
        add_campaign_save_btn = self.driver.find_element(*RealmaxCampaignPageLocators.add_campaign_save_btn)
        add_campaign_save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.ok_btn)
        ok_btn.click()

    def addContactToCampaign(self, campaign_name, contacts):
        time.sleep(3)
        action = actions.init(self.driver)
        action.click('campaign','contact_management', campaign_name)
        time.sleep(2)
        contact_tb = self.driver.find_element(*RealmaxCampaignPageLocators.tag_tb)
        for contact in contacts:
            time.sleep(2)
            contact_tb.send_keys(contact)
            time.sleep(3)
            contact_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-tagsautocomplete-list']")
            contact_auto_complete.click()
            contact_tb.clear()
        save_btn = self.driver.find_element(*RealmaxCampaignPageLocators.save_btn)
        save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.ok_btn)
        ok_btn.click()
        
    def deleteCampaign(self, campaign_name):
        time.sleep(3)
        action = actions.init(self.driver)
        action.click('campaign','delete', campaign_name)
        time.sleep(2)
        confirm_delete_ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.confirm_delete_ok_btn)
        confirm_delete_ok_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.ok_btn)
        ok_btn.click()