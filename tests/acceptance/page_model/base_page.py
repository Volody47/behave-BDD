from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.base_page import BasePageLocators



class BasePage():
    def __init__(self, browser):
        self.browser = browser


    @property
    def url(self):
        return 'https://litecart.stqa.ru/en'

    @property
    def title(self):
        return self.browser.find_element(*BasePageLocators.TITLE)



