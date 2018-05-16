from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from distributors.models import Person, CarShop, Model, Car, Sell, ModelReview
from distributors.forms import SellForm, CarShopForm, CarForm


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
    template_name = 'distributors/form.html'


# HTML Views

class ModelDetail(DetailView):
    model = Model
    template_name = 'distributors/model_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ModelDetail, self).get_context_data(**kwargs)
        return context


class SellerDetail(DetailView):
    model = Person
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
    model = Person
    template_name = 'distributors/customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        return context


class CustomerList(ListView):
    model = Person
    context_object_name = 'latest_customer_list'
    template_name = 'distributors/customer_list.html'


# class SellDetail(DetailView):
#    model = Sell
#  template_name = 'myapp/sell?detail'

class SellerList(ListView):
    model = Person
    context_object_name = 'latest_seller_list'
    template_name = 'distributors/seller_list.html'

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

class SellCreate(LoginRequiredMixin, CreateView):
    model = Sell
    template_name = 'distributors/form.html'
    form_class = SellForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(SellCreate, self).form_valid(form)


class CarShopCreate(LoginRequiredMixin, CreateView):
    model = CarShop
    template_name = 'distributors/form.html'
    form_class = CarShopForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.CarshopCreate = CarShop.objects.get(id=self.kwargs['pk'])
        return super(CarShopCreate, self).form_valid(form)

class CarShopDelete(DeleteView):
    model = CarShop
    #template_name = 'department_delete.html'
    template_name = 'distributors/carshop_delete.html'

    #def get_success_url(self):
     #   return reverse_lazy('department')

    def get_object(self, queryset=None):
        obj = super(CarShopDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse('distributors:carshop_list')

class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'distributors/form.html'
    form_class = CarForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.carshop = CarShop.objects.get(id=self.kwargs['pk'])
        return super(CarCreate, self).form_valid(form)






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