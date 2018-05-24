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


@step("I'm viewing the reviews containing")
def step_impl(context):
    reviews = context.browser.find_by_css('blockquote.review')
    for i, row in enumerate(context.table):
        assert reviews[i].find_by_css('.rating').first.text.count(u"\u2605") == int(row['rating'])
        if row['comment']:
            assert row['comment'] == reviews[i].find_by_tag('strong').first.text
        assert reviews[i].find_by_tag('footer').first.text.startswith(row['user'])


@step('list contains "{count:n}" review')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('blockquote.review'))


@step('There are "{count:n}" reviews')
def step_impl(context, count):
    from distributors.models import CarShopReview
    assert count == CarShopReview.objects.count()


@given("I'm not logged in")
def step_impl(context):
    context.browser.visit(context.get_url('logout')+'?next=/distributors/')
    assert context.browser.is_text_present('Login')


@given('Exists review at dealership "{shop_name}" by "{username}"')
def step_impl(context, shop_name, username):
    from distributors.models import Person
    user = Person.objects.get(name=username)
    from distributors.models import CarShop
    shop = CarShop.objects.get(shopName=shop_name)
    from distributors.models import CarShopReview
    for row in context.table:
        review = CarShopReview(shopName=shop, user=user)
        for heading in row.headings:
            setattr(review, heading, row[heading])
        review.save()