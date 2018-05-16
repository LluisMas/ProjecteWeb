from django.contrib import admin

from distributors import models

admin.site.register(models.Person)
admin.site.register(models.CarShop)
admin.site.register(models.Model)
admin.site.register(models.Car)
admin.site.register(models.Sell)
admin.site.register(models.ModelReview)