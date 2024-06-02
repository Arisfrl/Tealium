import os
from datetime import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser.casefold() == "chrome":
        driver = webdriver.Chrome()
    elif browser.casefold() == "edge":
        driver = webdriver.Edge()
    elif browser.casefold() == "firefox":
        driver = webdriver.Firefox()

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose the browser to run the tests with",
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report


def pytest_configure(config):
    config.metadata['Project Name'] = 'Tealium'
    config.metadata['Module Name'] = 'CustRegistration'
    config.metadata['Tester'] = 'Aritra'
    # config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
