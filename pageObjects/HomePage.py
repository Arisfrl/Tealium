from selenium.webdriver.common.by import By


class HomePage:
    # locators
    link_account_xpath = "//span[@class='label'][normalize-space()='Account']"
    link_myaccount_linktext = "My Account"
    link_mywishlist_linktext = "My Wishlist"
    link_mycart_linktext = "My Cart"
    link_checkout_linktext = "Checkout"
    link_register_linktext = "Register"
    link_login_linktext = "Log In"
    link_logout_linktext = "Log Out"
    img_tealium_xpath = "//img[@alt='TealiumEcommerce Demo']"

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # actions
    def click_account(self):
        self.driver.find_element(By.XPATH, self.link_account_xpath).click()

    def click_myaccount(self):
        self.driver.find_element(By.LINK_TEXT, self.link_myaccount_linktext).click()

    def click_mywishlist(self):
        self.driver.find_element(By.LINK_TEXT, self.link_mywishlist_linktext).click()

    def click_mycart(self):
        self.driver.find_element(By.LINK_TEXT, self.link_mycart_linktext).click()

    def click_checkout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_checkout_linktext).click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT, self.link_register_linktext).click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def click_logo_tealium(self):
        self.driver.find_element(By.XPATH, self.img_tealium_xpath).click()
