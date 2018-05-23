from behave import *

use_step_matcher("parse")


@when("I list dealerships")
def step_impl(context):
    context.browser.visit(context.get_url('distributors:carshop_list'))


@then("I'm viewing a list containing")
def step_impl(context):
    distributors_links = context.browser.find_by_css('a.carshop-link')

    for i, row in enumerate(context.table):
        assert row['shopName'] == distributors_links[i].text


@step("list contains {count:n} Dealerships")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('a.carshop-link'))