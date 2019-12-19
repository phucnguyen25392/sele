from locator.locators import RealmaxCompanyPageLocators
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class init(BasePage):

    def addnewcompany(self, code, name, access_token=None, refesh_token=None, address=None, website=None, phone=None, description=None):
        addnew_company_link = self.driver.find_element(*RealmaxCompanyPageLocators.addnew_company_link)
        addnew_company_link.click()
        time.sleep(2)
        code_tb = self.driver.find_element(*RealmaxCompanyPageLocators.code_tb)
        code_tb.send_keys(code)
        name_tb = self.driver.find_element(*RealmaxCompanyPageLocators.name_tb)
        name_tb.send_keys(name)
        if address:
            address_tb = self.driver.find_element(*RealmaxCompanyPageLocators.address_tb)
            address_tb.send_keys(address)
        if website:
            website_tb = self.driver.find_element(*RealmaxCompanyPageLocators.website_tb)
            website_tb.send_keys(website)
        if phone:
            phone_tb = self.driver.find_element(*RealmaxCompanyPageLocators.phone_tb)
            phone_tb.send_keys(phone)
        if description:
            description_tb = self.driver.find_element(*RealmaxCompanyPageLocators.description_tb)
            description_tb.send_keys(description)
        if access_token and refesh_token:
            access_token_tb = self.driver.find_element(*RealmaxCompanyPageLocators.accesstoken_tb)
            access_token_tb.send_keys(access_token)
            refesh_token_tb = self.driver.find_element(*RealmaxCompanyPageLocators.refresh_tb)
            refesh_token_tb.send_keys(refesh_token)
            time.sleep(2)
        save_btn = self.driver.find_element(*RealmaxCompanyPageLocators.save_btn)
        save_btn.click()
        time.sleep(5)
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()
        time.sleep(5)

    def deletecompany(self, code):
        WebDriverWait(self.driver,10).until(cond.title_is("Manage company"))
        del_sele_link = self.driver.find_element_by_xpath(".//table[@id='table_data']/tbody//tr[contains(.,'" + code + "')]//span[@title='Remove']")
        del_sele_link.click()
        time.sleep(5)
        confirm_delete_ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.confirm_delete_ok_btn)
        confirm_delete_ok_btn.click()
        time.sleep(2)
        ok_btn = self.driver.find_element(*RealmaxCompanyPageLocators.ok_btn)
        ok_btn.click()
