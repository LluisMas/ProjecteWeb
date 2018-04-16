from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
import datetime


class Person(models.Model):
    # Mirant la randomuser.api les dades que retorna, comunes per selle i customer son:
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    street = models.CharField(max_length=30, null=True)
    gender = models.IntegerField(choices=(
        (1, 'Male'),
        (2, 'Female'),
    ), default=1)
    city = models.CharField(max_length=30, null=True)
    postCode = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    phoneNumber = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)

    # si volem ficar foto del venedor/ client falta canviar el upload
    # image = models.ImageField(upload_to="myapp", blank=True, null=True)

    def __str__(self):
        return self.name


class CarShop(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    inaugurationYear = models.IntegerField(choices=[(x, x) for x in range(2000, 2019)], default=2018)
    shopName = models.CharField(max_length=30, null=True)
    addr = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.shopName + ' - ' + self.addr
    def __unicode__(self):
        return u"%s" % self.shopName

    def get_absolute_url(self):
        return reverse('distributors:carshop_list', kwargs={'pk': self.pk})


class Model(models.Model):
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 5)):
        year_dropdown.append((y, y))

    id = models.PositiveIntegerField(primary_key=True)
    modelName = models.CharField(max_length=30, null=True)
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

    def __str__(self):
        return self.modelName

    def __unicode__(self):
        return u"%s" % self.modelName

    def get_absolute_url(self):
        return reverse('distributors:model_list', kwargs={'pk': self.pk})


class Car(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    model = models.ForeignKey(Model, default=1)
    kms = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=30, default="Color")
    registrationYear = models.PositiveIntegerField(default=0)
    carShop = models.ForeignKey(CarShop, default=1)

    def __str__(self):
        return str(self.id)


class Seller(models.Model):
    info = models.ForeignKey(Person, default=1)
    shop = models.ForeignKey(CarShop, default=1)
    salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.info.name
    def __unicode__(self):
        return u"%s" % self.info.name

    def get_absolute_url(self):
        return reverse('distributors:seller_list', kwargs={'pk': self.pk})


class Customer(models.Model):
    info = models.ForeignKey(Person, default=1)
    shop = models.ForeignKey(CarShop, default=1)

    def __str__(self):
        return self.info.name
    def __unicode__(self):
        return u"%s" % self.info.name

    def get_absolute_url(self):
        return reverse('distributors:customer_list', kwargs={'pk': self.pk})


class Sell(models.Model):
    seller = models.ForeignKey(Seller, default=1)
    customer = models.ForeignKey(Customer, default=1)
    car = models.ForeignKey(Car, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.seller.info.name + ' - ' + self.car.model.__name__


class ModelReview(models.Model):
    # valorar on ficar-lo
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Customer, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date), str(self.rating) + " starts"

    # class Meta:
    #    abstract = True

# class Restaurant(models.Model):
#     name = models.TextField()
#     street = models.TextField(blank=True, null=True)
#     number = models.IntegerField(blank=True, null=True)
#     city = models.TextField(blank=True, null=True)
#     zipCode = models.TextField(blank=True, null=True)
#     stateOrProvince = models.TextField(blank=True, null=True)
#     country = models.TextField(blank=True, null=True)
#     telephone = models.TextField(blank=True, null=True)
#     url = models.URLField(blank=True, null=True)
#     user = models.ForeignKey(User, default=1)
#     date = models.DateField(default=date.today)
#
#     def __unicode__(self):
#         return u"%s" % self.name
#
#     def get_absolute_url(self):
#         return reverse('myapp:restaurant_detail', kwargs={'pk': self.pk})
#
#     def averageRating(self):
#         reviewCount = self.restaurantreview_set.count()
#         if not reviewCount:
#             return 0
#         else:
#             ratingSum = sum([float(review.rating) for review in self.restaurantreview_set.all()])
#             return ratingSum / reviewCount
#
# class Dish(models.Model):
#     name = models.TextField()
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
#     user = models.ForeignKey(User, default=1)
#     date = models.DateField(default=date.today)
#     image = models.ImageField(upload_to="myapp", blank=True, null=True)
#     restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes')
#
#     def __unicode__(self):
#         return u"%s" % self.name
#
#     def get_absolute_url(self):
#         return reverse('myapp:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})
#
# class Review(models.Model):
#     RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
#     rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
#     comment = models.TextField(blank=True, null=True)
#     user = models.ForeignKey(User, default=1)
#     date = models.DateField(default=date.today)
#
#     class Meta:
#         abstract = True
#
# class RestaurantReview(Review):
#     restaurant = models.ForeignKey(Restaurant)
#
#     class Meta:
#         unique_together = ("restaurant", "user")
