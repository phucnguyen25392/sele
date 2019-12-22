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
from config.setting import *

class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

class init(BaseAction):
    
    def click(self, element_type, action_type, element_name):
        # require element name
        if element_type == 'campaign':
            if action_type == 'delete':
                time.sleep(2)
                try:
                    delete_campaign_btn = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//div[@name='" + element_name + "']//span[@title='Remove']")
                except NoSuchElementException:
                    pass
                if delete_campaign_btn:
                    delete_campaign_btn.click()
            elif action_type == 'edit':
                time.sleep(2)
                try:
                    edit_campaign_btn = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//div[@name='" + element_name + "']//span[@title='Edit']")
                except NoSuchElementException:
                    pass
                if edit_campaign_btn:
                    edit_campaign_btn.click()
            elif action_type == 'contact_management':
                time.sleep(2)
                try:
                    managecontact_campaign_btn = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//div[@name='" + element_name + "']//span[@title='Contact management']")
                except NoSuchElementException:
                    pass
                if managecontact_campaign_btn:
                    managecontact_campaign_btn.click()
            else:
                pass
        # require element email
        if element_type == 'contact':
            if action_type == 'delete':
                time.sleep(2)
                try:
                    delete_contact = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//span[@title='Remove']")
                except NoSuchElementException:
                    pass
                if delete_contact:
                    delete_contact.click()
            elif action_type == 'edit':
                time.sleep(2)
                try:
                    edit_contact = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//span[@title='Edit']")
                except NoSuchElementException:
                    pass
                if edit_contact:
                    edit_contact.click()
            elif action_type == 'apply_tag':
                time.sleep(2)
                try:
                    apply_tag = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(.,'" + element_name + "')]//span[@title='Apply tags to this contact']")
                except NoSuchElementException:
                    pass
                if apply_tag:
                    apply_tag.click()
               
            

