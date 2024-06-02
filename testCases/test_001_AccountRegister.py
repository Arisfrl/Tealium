import os

import pytest

from pageObjects import HomePage
from pageObjects import Register
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestAccountRegistration:
    baseurl = ReadConfig.getApplicationUrl()
    # baseurl = 'https://ecommerce.tealiumdemo.com/'
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_account_register(self, setup):
        self.logger.info("Starting account registration")
        self.driver = setup
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)  # sec #wait
        # homepage
        self.homepage = HomePage.HomePage(self.driver)
        self.homepage.click_account()
        # time.sleep(5)
        self.homepage.click_register()

        # register
        self.register = Register.Register(self.driver)
        # time.sleep(5)
        self.register.set_firstname("Aritra")
        self.register.set_lastname("Biswas")
        # self.register.set_email(randomString.id_generator(10) + "@gmail.com")
        self.register.set_email(randomString.id_generator(10) + "@gmailcom")  # to create fail scenario.
        self.register.set_password("Password@123")
        self.register.set_confirm_password("Password@123")
        self.register.click_register()
        # time.sleep(5)
        flag = self.register.check_success_regestion()
        if flag:
            print(ReadConfig.getApplicationUrl())
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_register.png")
            print(os.path.abspath(os.curdir))
            self.logger.error("Register failed.")
            assert False
