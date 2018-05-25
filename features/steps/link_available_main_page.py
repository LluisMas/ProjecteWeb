from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

use_step_matcher("parse")


@given("I visit the main page")
def step_impl(context):
    context.browser.visit(context.get_url() + "/distributors/")


@then('There is "{text}" text available')
def step_impl(context, text):
    context.browser.is_element_present_by_name(text)


@then('There is no "{text}" text available')
def step_impl(context, text):
    context.browser.is_element_not_present_by_name(text)



