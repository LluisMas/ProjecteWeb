from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied, ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.http import urlquote
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from distributors.models import Person, CarShop, Car, Sell, CarShopReview
from distributors.forms import SellForm, CarShopForm, CarForm, EditCarShopForm
from distributorsapp import settings


class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class PermissionRequiredMixin(object):
    login_url = settings.LOGIN_URL
    permission_required = 'fitters.change_fitter'
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def dispatch(self, request, *args, **kwargs):
        # Verify class settings

        if request.user.is_authenticated:

            has_permission = request.user.type
            if has_permission == 1:
                if self.raise_exception:
                    return HttpResponseForbidden()
                else:
                    path = urlquote(request.get_full_path())
                    tup = self.login_url, self.redirect_field_name, path
                    return HttpResponseRedirect("%s?%s=%s" % tup)
        else:
            path = urlquote(request.get_full_path())
            tup = self.login_url, self.redirect_field_name, path
            return HttpResponseRedirect("%s?%s=%s" % tup)

        return super(PermissionRequiredMixin, self).dispatch(
            request, *args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        context_object_name = 'latest_person_list'
        template_name = 'distributors/person_list.html'


class LoginRequiredCheckIsOwnerUpdateView(CheckIsOwnerMixin, UpdateView):
    template_name = 'distributors/form.html'



# HTML Views

class CarDetail(DetailView):
    model = Car
    template_name = 'distributors/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CarDetail, self).get_context_data(**kwargs)
        return context

#
# class SellerDetail(DetailView):
#     model = Person
#     template_name = 'distributors/seller_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(SellerDetail, self).get_context_data(**kwargs)
#         return context
#

class CarList(ListView):
    model = Car
    context_object_name = 'latest_car_list'
    template_name = 'distributors/car_list.html'


class CarShopDetail(DetailView):
    model = CarShop
    template_name = 'distributors/carshop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CarShopDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = CarShopReview.RATING_CHOICES
        return context



class CarShopList(ListView):
    model = CarShop
    context_object_name = 'latest_carshop_list'
    template_name = 'distributors/carshop_list.html'

    class SellList(PermissionRequiredMixin, ListView):
        model = Sell
        context_object_name = 'latest_sells_list'
        template_name = 'distributors/sell_list.html'


class PersonDetail(PermissionRequiredMixin, DetailView):
    model = Person
    template_name = 'distributors/person_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PersonDetail, self).get_context_data(**kwargs)
        return context


class PersonList(PermissionRequiredMixin, ListView):
    model = Person
    context_object_name = 'latest_person_list'
    template_name = 'distributors/person_list.html'

class CarShopCreate(CreateView):
    model = CarShop
    template_name = 'distributors/form.html'
    form_class = CarShopForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.email = self.request.user.email
        #form.instance.CarshopCreate =  CarShop.objects.get(id=self.kwargs['pk'])
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

class CarCreate(CreateView):
    model = Car
    template_name = 'distributors/form.html'
    form_class = CarForm


    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.carShop = CarShop.objects.get(id=self.kwargs['pk'])
        return super(CarCreate, self).form_valid(form)


class CarDelete(DeleteView):
    model = Car
    #template_name = 'department_delete.html'
    template_name = 'distributors/cars_delete.html'

    #def get_success_url(self):
     #   return reverse_lazy('department')

    def get_object(self, queryset=None):
        obj = super(CarDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse('distributors:carshop_detail', kwargs={'pk':self.kwargs['pkr'],})


class CarEdit(PermissionRequiredMixin, UpdateView):
    model = Car
    #
    template_name_suffix = "_update_form"

class CarShopEdit(PermissionRequiredMixin, UpdateView):
    model = CarShop
    #exclude = ['user']
    form_class = EditCarShopForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarShopEdit, self).form_valid(form)
    #template_name_suffix = "_update_form"


class SellCreate(PermissionRequiredMixin, CreateView):#isSellermixing envez de LoginRequiredMixin extienda LoginREquired

    model = Sell
    template_name = 'distributors/sell_form.html'
    form_class = SellForm
    def form_valid(self, form):
        form.instance.seller = self.request.user
        form.instance.car = Car.objects.get(id=self.kwargs['pk'])

        car = Car.objects.get(pk=self.kwargs['pk'])
        car.availability = 2
        car.save()

        return super(SellCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SellCreate, self).get_context_data(**kwargs)
        context['car'] = Car.objects.get(pk=self.kwargs['pk'])
        return context



class SellList(PermissionRequiredMixin, ListView):
    model = Sell
    context_object_name = 'latest_sells_list'
    template_name = 'distributors/sell_list.html'


class SellDetail(PermissionRequiredMixin, DetailView):
    model = Sell
    template_name = 'distributors/sell_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SellDetail, self).get_context_data(**kwargs)
        return context

@login_required()
def review(request, pk):
    carshop = get_object_or_404(CarShop, pk=pk)
    if CarShopReview.objects.filter(shopName=carshop, user=request.user).exists():
        CarShopReview.objects.get(shopName=carshop, user=request.user).delete()
    new_review = CarShopReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        shopName=carshop)
    new_review.save()
    return HttpResponseRedirect(reverse('distributors:carshop_detail', args=(carshop.id,)))