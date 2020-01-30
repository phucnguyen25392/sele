from selenium.webdriver.common.by import By

class RealmaxLoginPageLocators(object):
    email_tb = (By.ID, 'email')
    password_tb = (By.ID, 'password')
    login_btn = (By.XPATH, './/button')
    realmax_img = (By.XPATH, ".//div[@id=\"header\"]//div[@class=\"navbar nav_title logo\"]//img")
    loginfailed_mess = (By.XPATH, ".//div[@class=\"panel-body\"]//div[@class=\"div-normal-login\"]//p[@class=\"danger\"]")

class RealmaxMainPageLocators(object):
    admin_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Administrator')]")
    company_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//li[contains(., 'Administrator')]//li[@title='company']//a")
    user_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//li[contains(., 'Administrator')]//li[@title='user']//a")
    mycompany_link = (By.XPATH, ".//div[@class='nav_menu']//ul[@class='nav navbar-nav navbar-right']//li[@class='open']//ul[@class='dropdown-menu dropdown-usermenu pull-right']//a[contains(.,'My company')]")
    userprofile_link = (By.XPATH, ".//div[@class='nav_menu']//ul[@class='nav navbar-nav navbar-right']//a[@class='user-profile dropdown-toggle']")
    dashboard_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Dashboard')]")
    contact_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Contact')]")
    new_contact_link = (By.XPATH,".//*[@id=\"sidebar-nav\"]//li[contains(., 'Contact')]//li[@title='new-contact']//a")
    manage_contact_link = (By.XPATH,".//*[@id=\"sidebar-nav\"]//li[contains(., 'Contact')]//li[@title='contact']//a")
    side_menu_open_link = (By.XPATH, ".//*[@class='container-fluid']//button[@class='btn-toggle-fullwidth']//i[@class='lnr lnr-arrow-right-circle']")
    side_menu_close_link = (By.XPATH, ".//*[@class='container-fluid']//button[@class='btn-toggle-fullwidth']//i[@class='lnr lnr-arrow-left-circle']")
    tag_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//li[contains(., 'Manage tag')]")
    campaign_link = (By.XPATH, ".//*[@id=\"sidebar-nav\"]//span[contains(text(),'Campaign')]")
    new_campaign_link = (By.XPATH,".//*[@id=\"sidebar-nav\"]//li[contains(., 'Campaign')]//li[@title='new-campaign']//a")
    manage_campaign_link = (By.XPATH,".//*[@id=\"sidebar-nav\"]//li[contains(., 'Campaign')]//li[@title='campaign']//a")
    admin_profile_link = (By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']//li[contains(., 'My Profile')]")
    admin_mycompany_link = (By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']//li[contains(., 'My company')]//ul[@class='dropdown-menu']//a[contains(., 'My company')]")
    admin_myprofile_link = (By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']//li[contains(., 'My Profile')]//ul[@class='dropdown-menu']//a[contains(., 'My Profile')]")
    noti_link = (By.XPATH, ".//ul[@class='nav navbar-nav navbar-right']/li[@class='dropdown dropdown-notif']")
    new_mess_link = (By.XPATH, ".//div[@id='btn-new-message']")

class RealmaxCompanyPageLocators(object):
    addnew_company_link = (By.XPATH, ".//div[@class='container-fluid']//a[contains(.,'New company')]")
    code_tb = (By.XPATH, "//*[@id=\"code\"]")
    name_tb = (By.XPATH, "//*[@id=\"name\"]")
    address_tb = (By.XPATH, "//*[@id='address']")
    website_tb = (By.XPATH, "//*[@id='website']")
    phone_tb = (By.XPATH, "//*[@id='phone']")
    description_tb = (By.XPATH, "//*[@id='description']")
    accesstoken_tb = (By.XPATH, "//*[@id=\"infusionAccessToken\"]")
    refresh_tb = (By.XPATH, "//*[@id=\"infusionRefreshToken\"]")
    save_btn = (By.XPATH, "//*[@class=\"btn btn-primary btn-flat btn-apply\"]")
    token_success_message = (By.XPATH, "//*[@id=\"ap-message-content\"]/span")
    checktoken_btn = (By.XPATH, "//*[@id=\"btn-check-infusion-auth\"]")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")
    confirm_delete_ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@id=\"btnConfirm\"]")
    token_invalid_message = (By.XPATH, ".//div[@class='modal-content']//p[contains(.,'Could not verify your Infusionsoft authentication info.')]")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")
    confirm_delete_ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@id=\"btnConfirm\"]")

class RealmaxUserPageLocators(object):
    addnew_user_btn = (By.XPATH, ".//div[@class='container-fluid']//a[contains(.,'New user')]")
    fname_tb = (By.XPATH, ".//input[@id='fisrtName']")
    lname_tb = (By.XPATH, ".//input[@id='lastName']")
    company_sb = (By.XPATH, ".//select[@id='select-company']")
    role_sb = (By.XPATH, ".//select[@id='select-role']")
    email_tb = (By.XPATH, ".//input[@id='email']")
    password_tb = (By.XPATH, ".//input[@id='password']")
    newpass_tb = (By.XPATH, ".//input[@id='new-password']")
    confirmpass_tb = (By.XPATH, ".//input[@id='confirm-password']")
    changepass_btn = (By.XPATH, ".//button[contains(.,'Change password')]")
    phone_tb = (By.XPATH, ".//input[@id='phone']")
    save_btn = (By.XPATH, "//*[@class=\"btn btn-primary btn-flat btn-apply\"]")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")
    confirm_delete_ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@id=\"btnConfirm\"]")
    viewlength_sb = (By.XPATH, "//select[@name='table_data_length']")
    new_mess_link = (By.XPATH, ".//div[@id='btn-new-message']")
    specific_user_ratio = (By.XPATH, ".//input[@value='2']")
    all_user_ratio = (By.XPATH, ".//input[@value='1']")
    mess_user_name_tb = (By.XPATH, ".//input[@id='input-auto-complete-message-users']")
    message_content_tb = (By.XPATH, ".//textarea[@id='txt-message-content']")
    attachment_content_tb = (By.XPATH, ".//textarea[@id='txt-message-link']")
    send_mess_btn = (By.XPATH, ".//button[@id='btn-send-message-to-user']")
    email_exist_mess = (By.XPATH, ".//div[@class='alert-warning alert']//ul[contains(.,'Your email is already existed')]")
    cancel_btn = (By.XPATH, "//*[@class='btn btn-danger  btn-flat']")

class RealmaxTagDialogLocator(object):
    tag_input = (By.XPATH, "//div[@class='modal-dialog']//input[@id='input-auto-complete-tags']")
    save_btn = (By.XPATH, ".//button[@class='btn btn-primary btn-save']")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")

class RealmaxContactPageLocators(object):
    # ui id is wrong "fisrt" temp handle 
    fname_tb = (By.XPATH, ".//*[@id='main-form']//div[@class='container']//div[contains(.,'First name')]//input[@id='fisrtName']")
    lname_tb = (By.XPATH, ".//*[@id='main-form']//div[@class='container']//div[contains(.,'Last name')]//input[@id='lastName']")
    email_tb = (By.XPATH, ".//*[@id='main-form']//div[@class='container']//div[contains(.,'Email')]//input[@id='email']")
    save_btn = (By.XPATH, ".//*[@class='btn btn-primary btn-flat btn-apply']")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")
    confirm_delete_ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@id=\"btnConfirm\"]")
    fname_search_tb = (By.XPATH, ".//input[@id='fisrtName']")
    email_search_tb = (By.XPATH, ".//input[@id='email']")
    tag_search_tb = (By.XPATH, ".//input[@id='input-auto-complete-tags-2']")
    search_btn = (By.XPATH, ".//button[@class='btn btn-primary btn-flat btn-search']")
    save_tag_btn = (By.XPATH, ".//button[@class='btn btn-primary btn-save']")

class RealmaxTagPageLocators(object):
    apply_vip_contact_link = (By.XPATH, ".//table[@id='table_data']//tr[contains(., '[VIP]')]//span[@title='Apply this tag to contacts']")
    save_btn = (By.XPATH, ".//button[@class='btn btn-primary btn-save']")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")

class RealmaxCampaignPageLocators(object):
    add_new_campaign_btn = (By.XPATH, ".//div[@class='container-fluid']//a[contains(.,'New campaign')]")
    name_tb = (By.XPATH, ".//input[@id='name']")
    tag_tb = (By.XPATH, ".//input[@id='input-auto-complete-tags']")
    user_tb = (By.XPATH, ".//input[@id='input-auto-complete-users']")
    save_btn = (By.XPATH, ".//button[@class='btn btn-primary btn-save']")
    add_campaign_save_btn = (By.XPATH, ".//a[@class='btn btn-primary btn-flat btn-apply']")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")
    confirm_delete_ok_btn = (By.XPATH, ".//button[@id='btnConfirm']")

class ProfilePageLocators(object):
    fname_tb = (By.XPATH, ".//input[@id='fisrtName']")
    lname_tb = (By.XPATH, ".//input[@id='lastName']")
    changepass_btn = (By.XPATH, ".//button[contains(.,'Change password')]")
    password_tb = (By.XPATH, ".//input[@id='password']")
    newpass_tb = (By.XPATH, ".//input[@id='new-password']")
    confirmpass_tb = (By.XPATH, ".//input[@id='confirm-password']")
    save_btn = (By.XPATH, "//*[@class=\"btn btn-primary btn-flat btn-apply\"]")
    ok_btn = (By.XPATH, ".//div[@class=\"modal-content\"]//button[@class=\"btn btn-primary\"]")