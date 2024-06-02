from selenium.webdriver.common.by import By


class Register:
    # locators
    txt_box_firstname_id = "firstname"
    txt_box_middle_name_id = "middlename"
    txt_box_lastname_id = "lastname"
    txt_box_email_id = "email_address"
    txt_box_password_id = "password"
    txt_box_confirm_password_id = "confirmation"
    checkbox_newsletter_id = "is_subscribed"
    checkbox_remember_me_xpath = "//input[@title='Remember Me']"
    btn_register_xpath = "//button[@title='Register']"
    link_back_xpath = "//a[@class='back-link']"
    text_err_msg_xpath = "//li[@class='error-msg']"
    text_success_msg_xpath = "//li[@class='success-msg']//span"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def set_firstname(self, name):
        self.driver.find_element(By.ID, self.txt_box_firstname_id).send_keys(name)

    def set_middle_name(self, name):
        self.driver.find_element(By.ID, self.txt_box_middle_name_id).send_keys(name)

    def set_lastname(self, name):
        self.driver.find_element(By.ID, self.txt_box_lastname_id).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.txt_box_email_id).send_keys(email)

    def set_password(self, pwd):
        self.driver.find_element(By.ID, self.txt_box_password_id).send_keys(pwd)

    def set_confirm_password(self, confirm_password):
        self.driver.find_element(By.ID, self.txt_box_confirm_password_id).send_keys(confirm_password)

    def click_newsletter(self):
        self.driver.find_element(By.ID, self.checkbox_newsletter_id).click()

    def click_remember_me(self):
        self.driver.find_element(By.XPATH, self.checkbox_remember_me_xpath).click()

    def click_register(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

    def click_back(self):
        self.driver.find_element(By.XPATH, self.link_back_xpath).click()

    def check_success_regestion(self) -> object:
        try:
            return self.driver.find_element(By.XPATH, self.text_success_msg_xpath).is_displayed()
        except:
            return False

