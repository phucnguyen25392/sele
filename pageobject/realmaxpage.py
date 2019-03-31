from locators import RealmaxLoginPageLocators
import time 

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def login(self, email, password):
        email_tb = self.driver.find_element(*RealmaxLoginPageLocators.email_tb)
        email_tb.send_keys(email)
        password_tb =  self.driver.find_element(*RealmaxLoginPageLocators.password_tb)
        password_tb.send_keys(password)
        login_btn = self.driver.find_element(*RealmaxLoginPageLocators.login_btn)
        login_btn.click()

    def logout(self):
        self.driver.get("https://www.realmax.ga/logout")
        time.sleep(10)

