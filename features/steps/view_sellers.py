from behave import *

use_step_matcher("parse")


@then("The list of Sellers is not displayed")
def step_impl(context):
    assert context.browser.url != context.get_url("distributors:seller_list")


@when("I view the list of Sellers")
def step_impl(context):
    context.browser.visit(context.get_url('distributors:seller_list'))


@then("The list of Sellers is displayed")
def step_impl(context):
    assert context.browser.url == context.get_url("distributors:seller_list")


@step('Customer list contains {count:n} seller')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('a.seller-link'))
