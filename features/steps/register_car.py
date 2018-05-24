from __future__ import print_function
from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse




use_step_matcher("parse")

@step('Exists a carshop with name "{shopName}" and email "{email}"')
def step_impl(context, shopName, email):
    from distributors.models import Person
    u= Person.objects.get(email=email)
    from distributors.models import CarShop
    CarShop.objects.create(inaugurationYear="1997", shopName=shopName, addr="Laverga",
                           country="Argentina", city="Franco", user=u)


@when('I register a car at carshop "{shopName}"')
def step_impl(context, shopName):
    from distributors.models import CarShop
    carShop = CarShop.objects.get(shopName=shopName)


    for row in context.table:
        context.browser.visit(context.get_url('distributors:add_car', carShop.pk))
        if context.browser.url == context.get_url('distributors:add_car', carShop.pk):
            form = context.browser.find_by_tag('form').first
            context.browser.fill("name","AnyShop")
            context.browser.fill("body", "Compacto")
            #context.browser.fill("price", "AnyPrice")

            form.find_by_css('button.btn-success').first.click()


@then('I\'m viewing the details page for car at carshop "{shopName}" by "{email}"')
def step_impl(context, shopName, email):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from distributors.models import Person
    q_list.append(Q(('user', Person.objects.get(email=email))))
    from distributors.models import CarShop
    q_list.append(Q(('carshop', CarShop.objects.get(shopName=shopName))))

    from distributors.models import Car
    user = Person.objects.get(email=email)
    shop = CarShop.objects.get(shopName=shopName)
    car = Car.objects.get(carShop__shopName=shopName, carShop__user__email=email)
    assert context.browser.url == context.get_url(car)

    from distributors.models import Car
    #car = Car.objects.get(shopName=carShop.shopName)

    #with open('some.txt', 'a') as the_file:
    #    the_file.write('Hello\n')

    #assert context.browser.url == context.get_url(car)



@step("There are {count:n} cars")
def step_impl(context, count):
    from distributors.models import Car
    assert count == Car.objects.count()


@step('Exists cars registered by "{username}"')
def step_impl(context, username):
    from distributors.models import Person
    user = Person.objects.get(email=username)
    from distributors.models import Car
    for row in context.table:
        car = Car(user=user)
        for heading in row.headings:
            setattr(car, heading, row[heading])
        car.save()