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
        #la data s'ha exlos s'ha de mirar com afegir-la automaticament
        #fields = ('seller', 'car', 'date', )
        exclude = ('seller', 'car')

class EditCarShopForm(ModelForm):

    class Meta:
        model = CarShop
        exclude = ('user', )


class CarShopForm(ModelForm):
    class Meta:
        model = CarShop
       # fields = ('id','inaugurationYear', 'shopName', 'addr', 'country', 'city', )
        exclude = ('user',)

    #def get_success_url(self):
    #    return reverse('profile-list')

class CarForm(ModelForm):
    class Meta:
        model = Car
        #fields = ('id','model', 'kms', 'price', 'color', 'registrationYear', 'carShop')
        exclude = ('carShop', 'availability', )