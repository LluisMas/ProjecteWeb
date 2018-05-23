from behave import *

use_step_matcher("parse")


@step('Exists a car with name "{car}"')
def step_impl(context, car):
    from distributors.models import Car
    Car.objects.create(name=car, body="sedan")


@when('I register sell for car "{car}"')
def step_impl(context, car):
    from distributors.models import Car
    car = Car.objects.get(name=car)
    for row in context.table:
        context.browser.visit(context.get_url('distributors:add_sell', car.pk))
        if context.browser.url == context.get_url('distributors:add_distributors'):
            form = context.browser.find_by_tag('form').first
            form.find_by_css('button.btn-success').first.click()


@then("I'm viewing the details of the sell")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("There are 1 sell")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass