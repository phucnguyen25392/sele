from locator.locators import RealmaxContactPageLocators
from locator.locators import RealmaxTagDialogLocator
from locator.locators import RealmaxMainPageLocators
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import common.actions as actions
import time


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def addnewcontact(self, fname, lname, email, permission=None):
        WebDriverWait(self.driver,10).until(cond.title_is("Contact"))
        fname_tb = self.driver.find_element(*RealmaxContactPageLocators.fname_tb)
        fname_tb.send_keys(fname)
        lname_tb = self.driver.find_element(*RealmaxContactPageLocators.lname_tb)
        lname_tb.send_keys(lname)
        email_tb = self.driver.find_element(*RealmaxContactPageLocators.email_tb)
        email_tb.send_keys(email)
        if permission:
            permission_sb = Select(self.driver.find_element_by_xpath(".//div[@id='div-custom-fields']//select[@class='custom-field form-control']"))
            permission_sb.select_by_visible_text(permission)
        save_btn = self.driver.find_element(*RealmaxContactPageLocators.save_btn)
        save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxContactPageLocators.ok_btn)
        ok_btn.click()

    def applyTagToContact(self, email, tag):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        time.sleep(3)
        action = actions.init(self.driver)
        action.click('contact', 'apply_tag', email)
        time.sleep(2)
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, "//div[@class='modal-dialog']//input[@id='input-auto-complete-tags']")))
        tag_input = self.driver.find_element(*RealmaxTagDialogLocator.tag_input)
        tag_input.send_keys(tag)
        time.sleep(5)
        tag = self.driver.find_element_by_xpath(".//div[@class='modal-content']//div[@class='modal-body']//div[@id='input-auto-complete-tagsautocomplete-list']//div[contains(.,'" + tag + "')]")
        tag.click()
        save_btn = self.driver.find_element(*RealmaxTagDialogLocator.save_btn)
        save_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*RealmaxContactPageLocators.ok_btn)
        ok_btn.click()

    def removeContact(self, email):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        try:
            side_menu_open_link = self.driver.find_elements(*RealmaxMainPageLocators.side_menu_open_link)
        except NoSuchElementException:
            pass
        if len(side_menu_open_link) > 0:
            pass
        else:
            side_menu_close_link = self.driver.find_element(*RealmaxMainPageLocators.side_menu_close_link)
            side_menu_close_link.click()
        time.sleep(3)
        remove_contact_link = self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + email + "')]//span[@title='Remove']")
        remove_contact_link.click()
        time.sleep(5)
        delete_confirm_btn = self.driver.find_element(*RealmaxContactPageLocators.confirm_delete_ok_btn)
        delete_confirm_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*RealmaxContactPageLocators.ok_btn)
        ok_btn.click()

    def searchContact(self, contact_email):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage contact"))
        email_search_tb = self.driver.find_element(*RealmaxContactPageLocators.email_search_tb)
        email_search_tb.send_keys(contact_email)
        time.sleep(2)
        search_btn = self.driver.find_element(*RealmaxContactPageLocators.search_btn)
        search_btn.click()
    
    def removeAllTagsInContact(self, contact_email):
        time.sleep(2)
        try:
            tags = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//button[@class='btn btn-remove-tag btn-xs pull-right']")
        except NoSuchElementException:
            pass
        while len(tags) > 0:
            time.sleep(2)
            tags[0].click()
            try:
                tags = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//button[@class='btn btn-remove-tag btn-xs pull-right']")
            except NoSuchElementException:
                pass 
        save_tag_btn = self.driver.find_element(*RealmaxContactPageLocators.save_tag_btn)
        save_tag_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxContactPageLocators.ok_btn)
        ok_btn.click()

    