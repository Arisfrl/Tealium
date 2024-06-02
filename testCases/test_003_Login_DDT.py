import os
import time

from selenium.webdriver.common.by import By
from utilities import XLUtiles
from pageObjects import HomePage, Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestAccountLogin:
    baseurl = ReadConfig.getApplicationUrl()
    # baseurl = 'https://ecommerce.tealiumdemo.com/'
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir) + "\\testData\\Tealium_LoginData.xlsx"

    def test_account_login(self, setup):
        self.logger.info("Starting test_003_Login_DDT")
        self.rows = XLUtiles.getRowCount(self.path, 'Sheet1')
        lst_status = []
        self.driver = setup
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # sec #wait

        self.homepage = HomePage.HomePage(self.driver)  # homepage
        self.login = Login.Login(self.driver)  # login-page

        for r in range(2, self.rows + 1):
            self.homepage.click_account()
            self.homepage.click_login()

            self.email = XLUtiles.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtiles.readData(self.path, 'Sheet1', r, 2)
            self.res = XLUtiles.readData(self.path, 'Sheet1', r, 3)

            self.logger.info("Email: " +self.email + " Password: " +self.password)
            self.login.enter_email(self.email)
            self.login.enter_password(self.password)
            # scroll down till the element is visible. --> arguments[0].scrollIntoView(
            flag = self.driver.find_element(By.XPATH, self.login.checkbox_remember_me_xpath)
            self.driver.execute_script("arguments[0].scrollIntoView()", flag)
            self.login.click_remember_me()
            self.login.click_login()
            print(lst_status)
            flag = self.login.check_successful_login()
            if self.res == "Valid":
                if flag:
                    lst_status.append("Pass")
                    self.logger.info("Login successful.")
                    self.homepage.click_account()
                    self.homepage.click_logout()
                    self.logger.info("Logged out.")
                    time.sleep(4)
                else:
                    lst_status.append("Fail")
                    self.logger.info("Login Failed.")

            elif self.res == "Invalid":
                if flag:
                    lst_status.append("Fail")
                    self.logger.info("Login successful.")
                    self.homepage.click_account()
                    self.homepage.click_logout()
                    self.logger.info("Logged out.")
                    time.sleep(4)
                else:
                    lst_status.append("Pass")
                    self.logger.info("Login Failed.")

            self.homepage.click_logo_tealium()
            self.logger.info("Directed to home page.")
            time.sleep(5)
            self.logger.info(self.driver.current_url)
            # Final Validation

            if "Fail" in lst_status:
                assert False
            else:
                assert True

            self.logger.info("End of test_003_Login_DDT")
