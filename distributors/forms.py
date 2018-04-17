from django.forms import ModelForm
from models import ModelReview



class ReviewForm(ModelForm):

    class Meta:
         model = ModelReview
         fields = ('user', 'comment', 'rating')
