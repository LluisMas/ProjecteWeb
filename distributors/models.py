from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Person(models.Model):
    #Mirant la randomuser.api les dades que retorna, comunes per selle i customer son:
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    postCode = models.IntegerField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    phoneNumber = models.IntegerField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    #si volem ficar foto del venedor/ client falta canviar el upload
   # image = models.ImageField(upload_to="myapp", blank=True, null=True)

    def __str__(self):
        return self.name

class CarShop(models.Model):
    id = models.IntegerField(primary_key=True)
    modelYear = models.IntegerField(blank=True, null=True)
    shopName = models.TextField(blank=True, null=True)
    addr = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.shopName + ' - ' + self.addr



class Model(models.Model):
    id = models.IntegerField(primary_key=True)
    modelName = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    fuelType = models.TextField(blank=True, null=True)
    modelYear = models.IntegerField(blank=True, null=True)
    maxTopSpeed = models.TextField(blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.modelName


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.ForeignKey(Model, default=1)
    kms = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    registrationYear = models.IntegerField(blank=True, null=True)
    carShop = models.ForeignKey(CarShop, default=1)

    def __str__(self):
        return str(self.id)

class Seller(models.Model):
    #nss = models.IntegerField(blank=True, null=True)
    info = models.ForeignKey(Person, default=1)
    shop = models.ForeignKey(CarShop, default=1)
    salary = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.info.name

class Customer(models.Model):
    info = models.ForeignKey(Person, default=1)
    shop = models.ForeignKey(CarShop, default=1)
    #sell = models.ForeignKey(Sell, default=1)

    def __str__(self):
        return self.info.name

class Sell(models.Model):
    seller = models.ForeignKey(Seller, default=1)
    customer = models.ForeignKey(Customer, default=1)
    car = models.ForeignKey(Car, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.seller.info.name + ' - ' + self.car.model.__name__



class ModelReview(models.Model):
    #valorar on ficar-lo
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Customer, default=1)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date), str(self.rating) + " starts"

    #class Meta:
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