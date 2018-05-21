from behave import *

use_step_matcher("parse")


@step('Exists a car with name "{car}"')
def step_impl(context, car):
    from distributors.models import Car
    Car.objects.create()
    pass


@step('Exists a Seller with name "{seller}"')
def step_impl(context, seller):
    """
    :type seller: str
    :type context: behave.runner.Context
    """
    pass


@when("I register sell")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


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