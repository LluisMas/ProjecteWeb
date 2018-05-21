from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}" and email "{email}"')
def step_impl(context, username, password, email):
    from distributors.models import Person
    Person.objects.create_user(name=username, email=email, password=password)


@given('I login as user "{email}" with password "{password}" and I am user "{user}"')
def step_impl(context, email, password, user):
    context.browser.visit(context.get_url('/accounts/login/?next=/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', email)
    context.browser.fill('password', password)
    form.find_by_css('button.btn-success').first.click()

    assert context.browser.is_text_present(email)


@when("I register dealership")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('distributors:add_distributors'))
        if context.browser.url == context.get_url('distributors:add_distributors'):
            form = context.browser.find_by_tag('form').first

            context.browser.fill("shopName","AnyShop")
            context.browser.fill("addr", "AnyPlace")
            form.find_by_css('button.btn-success').first.click()


@then('I\'m viewing the details page for dealership by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from distributors.models import Person
    q_list.append(Q(('user', Person.objects.get(email=username))))
    from distributors.models import CarShop
    user = Person.objects.get(email=username)
    carShop = CarShop.objects.get(user=user)
    assert context.browser.url == context.get_url(carShop)


@step("There are {count:n} dealerships")
def step_impl(context, count):
    from distributors.models import CarShop
    assert count == CarShop.objects.count()
