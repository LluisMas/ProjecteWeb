from __future__ import print_function
from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

@given('Exists dealership registered by "{username}"')
def step_impl(context, username):
    from distributors.models import Person
    user = Person.objects.get(name=username)
    from distributors.models import CarShop
    for row in context.table:
        carShop = CarShop(user=user)
        for heading in row.headings:
            setattr(carShop, heading, row[heading])
        carShop.save()

@when('I edit the dealership with name "{name}"')
def step_impl(context, name):
    from distributors.models import CarShop
    carShop = CarShop.objects.get(shopName=name)
    context.browser.visit(context.get_url('distributors:distributors_edit', carShop.pk))
    if context.browser.url == context.get_url('distributors:distributors_edit', carShop.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        context.browser.find_by_css('button.btn-success').first.click()

        file = open("verga.txt", "wa")
        file.write(context.get_url(carShop) + " Browser: " + context.browser.url)

        assert context.browser.url == context.get_url(carShop) + 'edit/'
