from locator.locators import RealmaxUserPageLocators
from locator.locators import RealmaxTagDialogLocator
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# Action
import common.actions as actions

import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def addNewUser(self, fname, lname, company, role, email, newpass, confirmpass, phone):
        WebDriverWait(self.driver,10).until(cond.title_is("User"))
        fname_tb = self.driver.find_element(*RealmaxUserPageLocators.fname_tb)
        fname_tb.send_keys(fname)
        lname_tb = self.driver.find_element(*RealmaxUserPageLocators.lname_tb)
        lname_tb.send_keys(lname)
        company_sb = Select(self.driver.find_element(*RealmaxUserPageLocators.company_sb))
        company_sb.select_by_visible_text(company)
        role_sb = Select(self.driver.find_element(*RealmaxUserPageLocators.role_sb))
        role_sb.select_by_visible_text(role)
        email_tb = self.driver.find_element(*RealmaxUserPageLocators.email_tb)
        email_tb.send_keys(email)
        newpass_tb = self.driver.find_element(*RealmaxUserPageLocators.newpass_tb)
        newpass_tb.send_keys(newpass)
        confirmpass_tb = self.driver.find_element(*RealmaxUserPageLocators.confirmpass_tb)
        confirmpass_tb.send_keys(confirmpass)
        phone_tb = self.driver.find_element(*RealmaxUserPageLocators.phone_tb)
        phone_tb.send_keys(phone)
        save_btn = self.driver.find_element(*RealmaxUserPageLocators.save_btn)
        save_btn.click()
        email_exist_mess = self.driver.find_elements(*RealmaxUserPageLocators.email_exist_mess)
        if len(email_exist_mess) > 0:
            cancel_btn = self.driver.find_element(*RealmaxUserPageLocators.cancel_btn)
            cancel_btn.click()
        else:
            time.sleep(10)
            ok_btn = self.driver.find_element(*RealmaxUserPageLocators.ok_btn)
            ok_btn.click()
    
    def editUser(self, email, fname, lname, new_pass):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(10)
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    edit_user_link = self.driver.find_elements_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + email + "')]//span[@title='Edit']")
                except NoSuchElementException:
                    pass
                if len(edit_user_link) == 0:
                    time.sleep(2)
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(3)
                    i += 1
                else:
                    time.sleep(2)
                    action = actions.init(self.driver)
                    action.click('user', 'edit', email)
                    time.sleep(3)
                    break
        WebDriverWait(self.driver,10).until(cond.title_is("User"))
        fname_tb = self.driver.find_element(*RealmaxUserPageLocators.fname_tb)
        fname_tb.clear()
        fname_tb.send_keys(fname)
        lname_tb = self.driver.find_element(*RealmaxUserPageLocators.lname_tb)
        lname_tb.clear()
        lname_tb.send_keys(lname)
        changepass_btn = self.driver.find_element(*RealmaxUserPageLocators.changepass_btn)
        changepass_btn.click()
        newpass_tb = self.driver.find_element(*RealmaxUserPageLocators.newpass_tb)
        newpass_tb.send_keys(new_pass)
        time.sleep(3)
        confirmpass_tb = self.driver.find_element(*RealmaxUserPageLocators.confirmpass_tb)
        confirmpass_tb.send_keys(new_pass)
        save_btn = self.driver.find_element(*RealmaxUserPageLocators.save_btn)
        save_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*RealmaxUserPageLocators.ok_btn)
        ok_btn.click()
    
    def deleteUser(self, email):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(10)
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    del_sele_link = self.driver.find_elements_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + email + "')]//span[@title='Remove']")
                except NoSuchElementException:
                    pass
                if len(del_sele_link) == 0:
                    time.sleep(2)
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(3)
                    i += 1
                else:
                    time.sleep(2)
                    action = actions.init(self.driver)
                    action.click('user', 'delete', email)
                    time.sleep(3)
                    break
        confirm_delete_ok_btn = self.driver.find_element(*RealmaxUserPageLocators.confirm_delete_ok_btn)
        confirm_delete_ok_btn.click()
        time.sleep(10)
        ok_btn = self.driver.find_element(*RealmaxUserPageLocators.ok_btn)
        ok_btn.click()

    def appplyTagToUser(self, email, tag):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    add_tag_link = self.driver.find_elements_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + email + "')]//span[@title='Grant Tag Permission']")
                except NoSuchElementException:
                    pass
                if len(add_tag_link) == 0:
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(5)
                    i += 1
                else:
                    time.sleep(2)
                    action = actions.init(self.driver)
                    action.click('user', 'apply_tag', email)
                    time.sleep(5)
                    break
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, "//div[@class='modal-dialog']//input[@id='input-auto-complete-tags']")))
        tag_input = self.driver.find_element(*RealmaxTagDialogLocator.tag_input)
        tag_input.send_keys(tag)
        time.sleep(5)
        tag = self.driver.find_element_by_xpath(".//div[@class='modal-content']//div[@class='modal-body']//div[@id='input-auto-complete-tagsautocomplete-list']//div[contains(.,'" + tag + "')]")
        tag.click()
        time.sleep(2)
        save_btn = self.driver.find_element(*RealmaxTagDialogLocator.save_btn)
        save_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxTagDialogLocator.ok_btn)
        ok_btn.click()

    def sendMessageToUsers(self, mess, attachment=None, names=None):
        new_mess_link = self.driver.find_element(*RealmaxUserPageLocators.new_mess_link)
        new_mess_link.click()
        time.sleep(3)
        if names:
            specific_user_ratio = self.driver.find_element(*RealmaxUserPageLocators.specific_user_ratio)
            specific_user_ratio.click()
            mess_user_name_tb = self.driver.find_element(*RealmaxUserPageLocators.mess_user_name_tb)
            for name in names:
                mess_user_name_tb.send_keys("sele")
                time.sleep(1)
                name_item = self.driver.find_element_by_xpath(".//div[@id='input-auto-complete-message-usersautocomplete-list']/div[contains(.,'" + name + "')]")
                name_item.click()
                mess_user_name_tb.clear()
                time.sleep(1)
        else:
            all_user_ratio = self.driver.find_element(*RealmaxUserPageLocators.all_user_ratio)
            all_user_ratio.click()
        time.sleep(3)
        message_tb = self.driver.find_element(*RealmaxUserPageLocators.message_content_tb)
        message_tb.send_keys(mess)
        attachment_tb = self.driver.find_element(*RealmaxUserPageLocators.attachment_content_tb)
        attachment_tb.send_keys(attachment)
        send_btn = self.driver.find_element(*RealmaxUserPageLocators.send_mess_btn)
        send_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxUserPageLocators.ok_btn)
        ok_btn.click()
        
    def removeAllTagsInUser(self, user_email):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage user"))
        time.sleep(2)
        try:
            pages = self.driver.find_elements(By.XPATH, ".//ul[@class='pagination']//li[@class='paginate_button page-item ']")
        except NoSuchElementException:
            pass
        if len(pages) > 0:
            i = 2
            while i <= len(pages) + 2:
                try:
                    add_tag_link = self.driver.find_elements_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + user_email + "')]//span[@title='Grant Tag Permission']")
                except NoSuchElementException:
                    pass
                if len(add_tag_link) == 0:
                    page_navigate_btn = self.driver.find_element(By.XPATH, ".//ul[@class='pagination']//a[contains(.,'" + str(i) + "')]")
                    page_navigate_btn.click()
                    time.sleep(5)
                    i += 1
                else:
                    action = actions.init(self.driver)
                    action.click('user', 'apply_tag', user_email)
                    time.sleep(5)
                    break
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, "//div[@class='modal-dialog']//input[@id='input-auto-complete-tags']")))
        try:
            remove_tags = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//button[@class='btn btn-remove-tag-permission btn-xs pull-right']")
        except NoSuchElementException:
            pass
        while len(remove_tags) > 0:
            time.sleep(2)
            remove_tags[0].click()
            try:
                remove_tags = self.driver.find_elements(By.XPATH, ".//div[@id='list-selected-tags']//button[@class='btn btn-remove-tag-permission btn-xs pull-right']")
            except NoSuchElementException:
                pass
        save_btn = self.driver.find_element(*RealmaxTagDialogLocator.save_btn)
        save_btn.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(*RealmaxTagDialogLocator.ok_btn)
        ok_btn.click()


