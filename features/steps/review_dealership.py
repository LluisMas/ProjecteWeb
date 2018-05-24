from behave import *

use_step_matcher("parse")


@when('I register a review at carshop "{shopName}"')
def step_impl(context, shopName):
    from distributors.models import CarShop
    carShop = CarShop.objects.get(shopName=shopName)
    for row in context.table:
        context.browser.visit(context.get_url(carShop))
        form = context.browser.find_by_tag('form').first
        context.browser.choose('rating', row['rating'])
        context.browser.fill('comment', row['comment'])
        form.find_by_tag('button').first.click()


@step('Exists dealership registered by the user "{email}" with name "{shop_name}"')
def step_impl(context, email, shop_name):
    from distributors.models import CarShop, Person
    user = Person.objects.get(email=email)
    carshop = CarShop(shopName=shop_name, user=user)
    carshop.addr="anyAddress"
    carshop.save()
