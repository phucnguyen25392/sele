from locator.locators import RealmaxMainPageLocators
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from locator.locators import ProfilePageLocators
#setting
from config.setting import *

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def edituserinfo(self, fname, lname, old_pass, new_pass):
        WebDriverWait(self.driver,10).until(cond.title_is("User"))
        fname_tb = self.driver.find_element(*ProfilePageLocators.fname_tb)
        fname_tb.clear()
        fname_tb.send_keys(fname)
        lname_tb = self.driver.find_element(*ProfilePageLocators.lname_tb)
        lname_tb.clear()
        lname_tb.send_keys(lname)
        changepass_btn = self.driver.find_element(*ProfilePageLocators.changepass_btn)
        changepass_btn.click()
        password_tb = self.driver.find_element(*ProfilePageLocators.password_tb)
        password_tb.send_keys(old_pass)
        time.sleep(2)
        newpass_tb = self.driver.find_element(*ProfilePageLocators.newpass_tb)
        newpass_tb.send_keys(new_pass)
        confirmpass_tb = self.driver.find_element(*ProfilePageLocators.confirmpass_tb)
        confirmpass_tb.send_keys(new_pass)
        time.sleep(2)
        save_btn = self.driver.find_element(*ProfilePageLocators.save_btn)
        save_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*ProfilePageLocators.ok_btn)
        ok_btn.click()

