from behave import *

use_step_matcher("parse")


@then("The list is not displayed")
def step_impl(context):
    assert context.browser.url != context.get_url("distributors:customer_list")


@when("I view the list of Customers")
def step_impl(context):
    context.browser.visit(context.get_url('distributors:customer_list'))


@then("The list is displayed")
def step_impl(context):
    assert context.browser.url == context.get_url("distributors:customer_list")


@step('Customer list contains {count:n} customers')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('a.customer-link'))
