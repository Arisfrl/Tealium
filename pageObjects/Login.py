from selenium.webdriver.common.by import By


class Login:
    # locators
    txt_box_email_id = "email"
    txt_box_password_id = "pass"
    btn_login_xpath = "//span[contains(text(),'Login')]"
    link_forgot_password_xpath = "//a[normalize-space()='Forgot Your Password?']"
    link_create_account_xpath = "//span[contains(text(),'Create an Account')]"
    checkbox_remember_me_xpath = "//input[@title='Remember Me']"
    txt_login_success_xpath = "//strong[normalize-space()='Hello, ARITRA BISWAS!']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # attributes
    def enter_email(self, email):
        self.driver.find_element(By.ID, self.txt_box_email_id).clear()
        self.driver.find_element(By.ID, self.txt_box_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.txt_box_password_id).clear()
        self.driver.find_element(By.ID, self.txt_box_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_create_account(self):
        self.driver.find_element(By.XPATH, self.link_create_account_xpath).click()

    def click_remember_me(self):
        self.driver.find_element(By.XPATH, self.checkbox_remember_me_xpath).click()

    def click_forgot_password(self):
        self.driver.find_element(By.XPATH, self.link_forgot_password_xpath).click()

    def check_successful_login(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_login_success_xpath).is_displayed()
        except:
            return False
