from django.forms import ModelForm
from models import ModelReview, Sell, CarShop



class ReviewForm(ModelForm):

    class Meta:
         model = ModelReview
         fields = ('user', 'comment', 'rating')


class SellForm(ModelForm):

    class Meta:
        model = Sell
        #la data s'ha exlos s'ha de mirar com afegir-la automaticament
        fields = ('seller', 'customer', 'car')

class CarShopForm(ModelForm):

    class Meta:
        model = CarShop
        #la data s'ha exlos s'ha de mirar com afegir-la automaticament
        #exlude = ()
        fields = ('id', 'inaugurationYear', 'shopName', 'addr')



