from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
import datetime


class Person(models.Model):
    # Mirant la randomuser.api les dades que retorna, comunes per seller i customer son:
    name = models.CharField(max_length=30, null=True)
    street = models.CharField(max_length=30, null=True)
    gender = models.IntegerField(choices=(
        (1, 'Male'),
        (2, 'Female'),
    ), default=1)
    city = models.CharField(max_length=30, null=True)
    postCode = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    phoneNumber = models.IntegerField(max_length=12, null=True)
    email = models.EmailField(max_length=70, blank=False, null=True)
    type = models.IntegerField(choices=(
        (1, 'Customer'),
        (2, 'Seller'),
        (3, 'Administrator')
        ), default=1)

    # En futures versions es ficara foto del venedor/ client
    # image = models.ImageField(upload_to="myapp", blank=True, null=True)

    def __str__(self):
        return self.name


    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('distributors:customer_list', kwargs={'pk': self.pk})

# class Model(models.Model):
#     year_dropdown = []
#     for y in range(2011, (datetime.datetime.now().year + 5)):
#         year_dropdown.append((y, y))
#
#     id = models.PositiveIntegerField(primary_key=True)
#     modelName = models.CharField(max_length=30, null=True)
#     body = models.CharField(max_length=30, null=True)
#     fuelType = models.IntegerField(choices=(
#         (1, 'Gasoline'),
#         (2, 'Diesel'),
#         (3, 'Electric'),
#         (4, 'Hybrid')
#     ), default=1)
#     modelYear = models.IntegerField(choices=[(x, x) for x in range(2000, 2019)], default=2018)
#     maxTopSpeed = models.PositiveIntegerField(validators=[MaxValueValidator(500)], default=0)
#     doors = models.IntegerField(choices=(
#         (1, '3 Doors'),
#         (2, '5 Doors')
#     ), default=2)
#     seats = models.IntegerField(choices=[(x, x) for x in range(2, 10)], default=5)
#
#     def __str__(self):
#         return self.modelName
#     def __unicode__(self):
#         return u"%s" % self.modelName
#
#     def get_absolute_url(self):
#         return reverse('distributors:model_list', kwargs={'pk': self.pk})



class CarShop(models.Model):
    inaugurationYear = models.IntegerField(choices=[(x, x) for x in range(2000, 2019)], default=2018)
    shopName = models.CharField(max_length=30, null=True)
    addr = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zipCode = models.CharField(max_length=120, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=120, blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __str__(self):
        space = " - "
        return "{} {} {}".format(self.shopName, space, self.addr)

    def __unicode__(self):
        return u"%s" % self.shopName

    def get_absolute_url(self):
        return reverse('distributors:carshop_detail', kwargs={'pk': self.pk})

class Car(models.Model):
    name = models.CharField(max_length=30, null=True)

    #model = models.ForeignKey(Model, default=1)
    kms = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=30, default="Color")
    registrationYear = models.PositiveIntegerField(default=0)
    carShop = models.ForeignKey(CarShop, null=True, related_name='cars')


    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 5)):
        year_dropdown.append((y, y))
    body = models.CharField(max_length=30, null=True)
    fuelType = models.IntegerField(choices=(
        (1, 'Gasoline'),
        (2, 'Diesel'),
        (3, 'Electric'),
        (4, 'Hybrid')
        ), default=1)
    modelYear = models.IntegerField(choices=[(x, x) for x in range(2000, 2019)], default=2018)
    maxTopSpeed = models.PositiveIntegerField(validators=[MaxValueValidator(500)], default=0)
    doors = models.IntegerField(choices=(
        (1, '3 Doors'),
        (2, '5 Doors')
    ), default=2)
    seats = models.IntegerField(choices=[(x, x) for x in range(2, 10)], default=5)

    availability = models.IntegerField(choices=(
        (1, 'Available'),
        (2, 'Sold')
    ), default=1)




    def __str__(self):
        return '1 - ' + str(self.name)

    def setSold(self):
        self.availability = 2

    def get_absolute_url(self):
        return reverse('distributors:car_detail', kwargs={'pkr': self.carshop.pk, 'pk': self.pk})


class Sell(models.Model):
    seller = models.ForeignKey(Person, default=1)
    car = models.ForeignKey(Car, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.seller.name + ' - ' + self.car.name

    def get_absolute_url(self):
        return reverse('distributors:sell_detail', kwargs={'pkr': self.car.pk, 'pk': self.pk})


class ModelReview(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Person, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date), str(self.rating) + " starts" 