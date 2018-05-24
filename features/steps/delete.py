from behave import *

use_step_matcher("parse")


@when('I view the details for car "{car}"')
def step_impl(context, car):
    from distributors.models import Car
    car = Car.objects.get(name=car)
    context.browser.visit(context.get_url(car))


@then('There is "{link}" link available')
def step_impl(context, link):
    assert context.browser.is_element_present_by_xpath('//a[text()="' + link + '"]')


@then('There is not "{link}" link available')
def step_impl(context, link):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="' + link + '"]')