from behave import *
from django.db.models import Q


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
        if context.browser.url == context.get_url('distributors:add_sell', car.pk):
            form = context.browser.find_by_tag('form').first
            form.find_by_css('button.btn-success').first.click()


@then('I\'m viewing the details of the sell "{sell}"')
def step_impl(context, sell):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from distributors.models import Car
    q_list.append(Q(('car', Car.objects.get(name=sell))))
    from distributors.models import Sell
    car = Car.objects.get(name=sell)
    sell_l = Sell.objects.get(car=car)
    assert context.browser.url == context.get_url(sell_l)


@step("There are {count:n} sell")
def step_impl(context, count):
    from distributors.models import Sell
    assert count == Sell.objects.count()


@step('Car "{car}" is set as sold')
def step_impl(context, car):
    from distributors.models import Car
    car_obj = Car.objects.get(name=car)
    assert car_obj.availability == 2
