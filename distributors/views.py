from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from distributors.models import *


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
    template_name = 'distributors/model_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDetail, self).get_context_data(**kwargs)
        return context


class SellerDetail(DetailView):
    model = Seller
    template_name = 'distributors/seller_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SellerDetail, self).get_context_data(**kwargs)
        return context


class ModelList(ListView):
    model = Model
    context_object_name = 'latest_model_list'
    template_name = 'distributors/model_list.html'


class CarShopDetail(DetailView):
    model = CarShop
    template_name = 'distributors/carshop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CarShopDetail, self).get_context_data(**kwargs)
        return context


class CarShopList(ListView):
    model = CarShop
    context_object_name = 'latest_carshop_list'
    template_name = 'distributors/carshop_list.html'


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'distributors/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        return context


class CustomerList(ListView):
    model = Customer
    context_object_name = 'latest_customer_list'
    template_name = 'distributors/customer_list.html'


# class SellDetail(DetailView):
#    model = Sell
#  template_name = 'myapp/sell?detail'

class SellerList(ListView):
    model = Seller
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

class PersonDetail(DetailView):
    model = Person
    template_name = 'distributors/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PersonDetail, self).get_context_data(**kwargs)
        return context


class PersonList(ListView):
    model = Person
    context_object_name = 'latest_person_list'
    template_name = 'distributors/person_list.html'

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