from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

from tests.acceptance.locators.main_page import MainPageLocators
from tests.acceptance.page_model.main_page import MainPage

use_step_matcher('re')


@when('I looking for "(.*)"')
def step_impl(context, products):
    page = MainPage(context.browser).search_products



@step('I count the "(.*)"')
def step_impl(context, stickers):
    page = MainPage(context.browser).search_products
    i = 0
    for sticker in page:
        stickers = page[i].find_elements(*MainPageLocators.STICKERS)
        context.stickers = stickers
        i += 1

