from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from models import Person, CarShop, Model, Car, Seller, Customer, Sell, ModelReview
# from forms import PersonForm, CarShopForm, ModelForm, SellerForm, SellForm, ReviewForm, CarForm

# Security Mixins

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'myapp/form.html'

# HTML Views

class ModelDetail(DetailView):
    model = Model
    template_name = 'myapp/model_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = ModelReview.RATING_CHOICES
        return context

class ModelList(ListView):
    model = Model
    context_object_name = 'latest_model_list'
    template_name = 'distributors/model_list.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'myapp/car_detail.html'

class CarList(ListView):
    model = Car
    template_name = 'myapp/car_list.html'


# class CarShopDetails(DetailView):
#     model = CarShop
#     template_name = 'distributors/carshop_details.html'
#     def get_context_data(self, **kwargs):
#         context = super(CarShopDetails, self).get_context_data(**kwargs)
#         return context

class CarShopList(ListView):
    model = CarShop
    context_object_name = 'latest_carshop_list'
    template_name = 'distributors/carshop_list.html'


class SellerDetails(DetailView):
    model = Seller
    template_name = 'myapp/seller_detail'

class CustomerDetails(DetailView):
    model = Customer
    template_name = 'myapp/car_detail'

class CustomerList(ListView):
    model = Customer
    context_object_name = 'latest_customer_list'
    template_name = 'distributors/customer_list.html'


class SellDetail(DetailView):
    model = Sell
    template_name = 'myapp/sell?detail'

class SellList(ListView):
    model = Sell
    context_object_name = 'latest_seller_list'
    template_name = 'distributors/seller_list.html'


# class RestaurantCreate(LoginRequiredMixin, CreateView):
#     model = Restaurant
#     template_name = 'myapp/form.html'
#     form_class = RestaurantForm
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super(RestaurantCreate, self).form_valid(form)

# class DishCreate(LoginRequiredMixin, CreateView):
#     model = Dish
#     template_name = 'myapp/form.html'
#     form_class = DishForm
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
#         return super(DishCreate, self).form_valid(form)

@login_required()
def review(request, pk):
    model = get_object_or_404(Model, pk=pk)
    new_review = ModelReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        model=model)
    new_review.save()
    return HttpResponseRedirect(reverse('myapp:restaurant_detail', args=(model.id,)))