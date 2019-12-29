from locator.locators import RealmaxTagPageLocators
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as cond
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def removeContagInTag(self, tag, contact):
        time.sleep(2)
        apply_tag_contact_link = self.driver.find_element_by_xpath(".//table[@id='table_data']//tr[contains(., '" + tag + "')]//span[@title='Apply this tag to contacts']")
        apply_tag_contact_link.click()
        WebDriverWait(self.driver,10).until(cond.visibility_of_any_elements_located((By.XPATH, ".//div[@class='modal-content']//div[@class='modal-header']//h4[contains(., 'Manage applied contact(s) of tag')]")))
        remove_contact_btn = self.driver.find_element_by_xpath(".//div[@id='list-selected-tags']//div[contains(., '" + contact + "')]//button[@class='btn btn-remove btn-xs pull-right']")
        remove_contact_btn.click()
        save_btn = self.driver.find_element(*RealmaxTagPageLocators.save_btn)
        save_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxTagPageLocators.ok_btn)
        ok_btn.click()
        

