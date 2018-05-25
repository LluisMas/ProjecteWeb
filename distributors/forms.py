from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from models import Sell, CarShop, Car
from models import Sell, CarShop, Car, Person



class SellerForm(ModelForm):
    class Meta:
        model = Person
        exclude = ('salary',)


class SellForm(ModelForm):

    class Meta:
        model = Sell
        exclude = ('seller', 'car')

class EditCarShopForm(ModelForm):

    class Meta:
        model = CarShop
        exclude = ('user', )


class CarShopForm(ModelForm):
    class Meta:
        model = CarShop
        exclude = ('user',)


class CarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ('carShop', 'availability', )