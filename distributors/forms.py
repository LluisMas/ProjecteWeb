from django.forms import ModelForm
from models import ModelReview, Sell, CarShop, Car, Person



class SellerForm(ModelForm):
    class Meta:
        model = Person
        exclude = ('salary',)



class ReviewForm(ModelForm):

    class Meta:
         model = ModelReview
         fields = ('user', 'comment', 'rating')


class SellForm(ModelForm):

    class Meta:
        model = Sell
        #la data s'ha exlos s'ha de mirar com afegir-la automaticament
        fields = ('seller', 'car')

class CarShopForm(ModelForm):
    class Meta:
        model = CarShop
       # fields = ('id','inaugurationYear', 'shopName', 'addr', 'country', 'city', )
        exclude = ('user', 'date', 'zipCode', )

    #def get_success_url(self):
    #    return reverse('profile-list')

class CarForm(ModelForm):
    class Meta:
        model = Car
        #fields = ('id','model', 'kms', 'price', 'color', 'registrationYear', 'carShop')
        exclude = ('carShop',)
       # def get_success_url(self):
        #    return reverse('profile-list')

        #class Car(models.Model):
        #    id = models.PositiveIntegerField(primary_key=True)
        #    model = models.ForeignKey(Model, default=1)
        #    kms = models.PositiveIntegerField(default=0)
        #    price = models.PositiveIntegerField(default=0)
        #    color = models.CharField(max_length=30, default="Color")
        #    registrationYear = models.PositiveIntegerField(default=0)
        #    carShop = models.ForeignKey(CarShop, default=1, related_name='cars')
