from django.forms import ModelForm
from models import ModelReview, Sell, CarShop, Seller



class SellerForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ('salary',)



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
        fields = ('id','inaugurationYear', 'shopName', 'addr')

    #def get_success_url(self):
    #    return reverse('profile-list')


