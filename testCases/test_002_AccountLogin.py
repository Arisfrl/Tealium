import os

import pytest
from selenium.webdriver.common.by import By

from pageObjects import HomePage, Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestAccountLogin:
    baseurl = ReadConfig.getApplicationUrl()
    # baseurl = 'https://ecommerce.tealiumdemo.com/'
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_login(self, setup):
        self.logger.info("Starting account login")
        self.driver = setup
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)  # sec #wait
        # homepage
        self.homepage = HomePage.HomePage(self.driver)
        self.homepage.click_account()
        self.homepage.click_login()

        self.login = Login.Login(self.driver)
        self.login.enter_email(ReadConfig.getEmail())
        self.login.enter_password(ReadConfig.getPassword())
        # scroll down till the element is visible. --> arguments[0].scrollIntoView()
        flag = self.driver.find_element(By.XPATH, self.login.checkbox_remember_me_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", flag)
        self.login.click_remember_me()
        self.login.click_login()

        flag = self.login.check_successful_login()
        if flag:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_login.png")
            print(os.path.abspath(os.curdir))
            self.logger.error("Login failed.")
            assert False
