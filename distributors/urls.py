from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, TemplateView
from distributors.models import CarShop, Person, Car, Sell
from distributors.views import CarList, PersonList, PersonDetail, SellerDetail, CustomerList, CustomerDetail, \
    CarShopList, \
    CarDetail, CarShopDetail, CarShopCreate, LoginRequiredCheckIsOwnerUpdateView, CarShopDelete, CarCreate, SellCreate, \
    SellList, SellDetail

from forms import CarShopForm, CarForm

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(
            template_name="distributors/home_page.html"),
        name="Principal"),

    url(r'^car/$',
        CarList.as_view(
            context_object_name='latest_car_list',
            template_name='distributors/car_list.html'),
        name='car_list'),

    url(r'^car/(?P<pk>\d+)/$',
        CarDetail.as_view(
            model=Car,
            template_name='distributors/car_detail.html'),
        name='car_detail'),

    url(r'^seller/$',
        PersonList.as_view(
            context_object_name='latest_person_list',
            template_name='distributors/seller_list.html'),
        name='seller_list'),

    url(r'^seller/(?P<pk>\d+)/$',
        PersonDetail.as_view(
            model=Person,
            template_name='distributors/seller_detail.html'),
        name='seller'),

    url(r'^customer/$',
        PersonList.as_view(
            context_object_name='latest_person_list',
            template_name='distributors/customer_list.html'),
        name='customer_list'),

    url(r'^customer/(?P<pk>\d+)/$',
        PersonDetail.as_view(
            model=Person,
            template_name='distributors/customer_detail.html'),
        name='customer_detail'),

  #  url(r'^carshop/$',
   #     CarShopList.as_view(
    #        # context_object_name = 'latest_movie_list',
     #       model=CarShop,
      #      context_object_name='latest_carshop_list',
       #     template_name='distributors/carshop_list.html'),
       # name='carshop_list'),

    url(r'^carshop/$',
        CarShopList.as_view(
            context_object_name='latest_carshop_list',
            template_name='distributors/carshop_list.html'),
        name='carshop_list'),


    url(r'^carshop/(?P<pkr>\d+)/cars/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Car,
            template_name='distributors/car_detail.html'),
        name='car_detail'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^carshop/(?P<pk>\d+)/$',
        CarShopDetail.as_view(),
        name='carshop_detail'),



    url(r'^person/$',
        PersonList.as_view(
            context_object_name='latest_person_list',
            template_name='distributors/person_list.html'),
        name='person_list'),

    url(r'^person/(?P<pk>\d+)/$',
        PersonDetail.as_view(
            model=Person,
            template_name='distributors/person_detail.html'),
        name='person_detail'),


    url(r'^add_sell/$',
        SellCreate.as_view(),
        name='sell_create'),

    # Create CarShop details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^carshop/create/$',
        CarShopCreate.as_view(),
        name='add_distributors'),


    # Edit CarShop details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^carshop/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=CarShop,
            form_class=CarShopForm),
        name='distributors_edit'),

    # Edit CarShop details, ex.: /myrestaurants/restaurants/1/delete/
    url(r'^carshop/(?P<pk>\d+)/delete/$',
        CarShopDelete.as_view(
        template_name = 'distributors/carshop_delete.html'),
        name='distributors_delete'),

    # Create CarShop details, ex.: /myrestaurants/restaurants/1/edit/
    # url(r'^carshop/(?P<pk>\d+)/create/$',
    #     LoginRequiredCheckIsOwnerUpdateView.as_view(
    #         model=Car,
    #         form_class=CarForm),
    #         name='add_car'),

    url(r'^carshop/(?P<pk>\d+)/create/$',
         CarCreate.as_view(),
         name='add_car'),

    url(r'^car/(?P<pk>\d+)/create/$',
        SellCreate.as_view(),
        name='add_sell'),

    url(r'^car/(?P<pkr>\d+)/sells/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Sell,
            template_name='distributors/sell_detail.html'),
        name='sell_detail'),

    url(r'^sells/$',
        SellList.as_view(
            context_object_name='latest_sells_list',
            template_name='distributors/sell_list.html'),
        name='sell_list'),

    url(r'^sells/(?P<pk>\d+)/$',
        SellDetail.as_view(),
        name='sell_detail'),

    #r'^carshop/(?P<pk>\d+)/create/$'


]