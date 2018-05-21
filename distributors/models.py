from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
import datetime

from distributorsapp import settings


class UserManager(BaseUserManager):
    def create_user(self, email, name, type, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            type=type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, type, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            type=type
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Person(AbstractBaseUser, PermissionsMixin):#BaseModeUser
    # Mirant la randomuser.api les dades que retorna, comunes per seller i customer son:
    name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, default="root")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        default="email@email.com"
    )

    is_admin = models.BooleanField(default=False)

    phoneNumber = models.IntegerField(max_length=12, null=True)
    street = models.CharField(max_length=30, null=True)
    gender = models.IntegerField(choices=(
        (1, 'Male'),
        (2, 'Female'),
    ), default=1)
    city = models.CharField(max_length=30, null=True)
    postCode = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    #email = models.EmailField(max_length=70, blank=False, null=True)
    type = models.IntegerField(choices=(
        (1, 'Customer'),
        (2, 'Seller')
    ), default=1)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'type']


    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        # if type == 2:
        return True
        # else:
        #     return False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    # En futures versions es ficara foto del venedor/ client
    # image = models.ImageField(upload_to="myapp", blank=True, null=True)

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')



    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s' % (self.name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.name
    #
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     '''
    #     Sends an email to this User.
    #     '''
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('distributors:customer_list', kwargs={'pk': self.pk})



class CarShop(models.Model):
    inaugurationYear = models.IntegerField(choices=[(x, x) for x in range(2000, 2019)], default=2018)
    shopName = models.CharField(max_length=30, null=True)
    addr = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    zipCode = models.CharField(max_length=120, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=120, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        space = " - "
        return "{} {} {}".format(self.shopName, space, self.addr)

    def __unicode__(self):
        return u"%s" % self.shopName

    def get_absolute_url(self):
        return reverse('distributors:carshop_detail', kwargs={'pk': self.pk})


class Car(models.Model):

    name = models.CharField(max_length=30, null=True)
    # model = models.ForeignKey(Model, default=1)
    kms = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=30, default="Color")
    registrationYear = models.PositiveIntegerField(default=0)
    carShop = models.ForeignKey(CarShop, null=True, related_name='cars')
    #user = carShop.user

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

    def get_absolute_url(self):
        return reverse('distributors:car_detail', kwargs={'pkr': self.carShop.pk, 'pk': self.pk})

    #return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})


class Sell(models.Model):
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
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
