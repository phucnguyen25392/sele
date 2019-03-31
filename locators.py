from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')

class RealmaxLoginPageLocators(object):
    email_tb = (By.ID, 'email')
    password_tb = (By.ID, 'password')
    login_btn = (By.ID, 'login')

class RealmaxMainPageLocators(object):
    admin_link = (By.XPATH, './/*[@id="sidebar-menu"]//span[contains(text(),'Administrator')]') 

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass