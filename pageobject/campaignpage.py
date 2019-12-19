from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locator.locators import RealmaxCampaignPageLocators
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def addNewCampaign(self, name, tags, users):
        WebDriverWait(self.driver,10).until(cond.title_is("Campaign"))
        name_tb = self.driver.find_element(*RealmaxCampaignPageLocators.name_tb)
        name_tb.send_keys(name)
        tag_tb = self.driver.find_element(*RealmaxCampaignPageLocators.tag_tb)
        for tag in tags:
            tag_tb.send_keys(tag)
            time.sleep(1)
            tag_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-tagsautocomplete-list']")
            tag_auto_complete.click()
            tag_tb.clear()
        user_tb = self.driver.find_element(*RealmaxCampaignPageLocators.user_tb)
        for user in users:
            user_tb.send_keys(user)
            time.sleep(1)
            user_auto_complete = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-usersautocomplete-list']")
            user_auto_complete.click()
            user_tb.clear()
        save_btn = self.driver.find_element(*RealmaxCampaignPageLocators.save_btn)
        save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxCampaignPageLocators.ok_btn)
        ok_btn.click()
