from django.forms import ModelForm
from models import ModelReview, Sell



class ReviewForm(ModelForm):

    class Meta:
         model = ModelReview
         fields = ('user', 'comment', 'rating')

class SellForm(ModelForm):
    model = Sell
    fields = ('seller', 'customer', 'car')



