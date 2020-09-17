from selenium import webdriver
from behave import *

from tests.acceptance.page_model.main_page import MainPage

use_step_matcher('re')




@given("I open url")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    page = MainPage(context.browser)
    context.browser.get(page.url)


@then("I'm on the home page")
def step_impl(context):
    expected_url = MainPage(context.browser).url
    assert context.browser.current_url == expected_url

@then("each product should have only one sticker")
def step_impl(context):
    assert len(context.stickers) == 1, "Should be just one sticker for each item"
