from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=username, email='user@example.com', password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/myrestaurants/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_css('button.btn-success').first.click()

    assert context.browser.is_text_present(username)


@when("I register dealership")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('distributors:add_distributor'))
        if context.browser.url == context.get_url('distributors:add_distributor'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_css('button.btn-success').first.click()


@then('I\'m viewing the details page for dealership by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from distributors.models import CarShop
    carShop = CarShop.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(carShop)


@step("There are {count:n} dealerships")
def step_impl(context, count):
    from distributors.models import CarShop
    assert count == CarShop.objects.count()
