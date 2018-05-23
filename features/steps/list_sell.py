from behave import *

use_step_matcher("parse")


@when("I list sells")
def step_impl(context):
    context.browser.visit(context.get_url('distributors:sell_list'))


@step("Exists cars registered")
def step_impl(context):
    for row in context.table:
        from distributors.models import Car
        car = Car()
        for heading in row.headings:
            setattr(car, heading, row[heading])
        car.save()


@step('list contains {count:n} sells')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('a.sell-link'))


@step('all of them are sold by user "{username}"')
def step_impl(context, username):
    for row in context.table:
        from distributors.models import Car, Sell, Person
        user = Person.objects.get(email=username)
        for heading in row.headings:
            car = Car.objects.get(name=row[heading])
            sell = Sell.objects.create(car=car, seller=user)


@then("I'm viewing a list containing those sells")
def step_impl(context):
    from distributors.models import Sell
    assert Sell.objects.count() == 6
    distributors_links = context.browser.find_by_css('a.sell-link')
    for i, row in enumerate(context.table):
        assert row['name'] == distributors_links[i].text