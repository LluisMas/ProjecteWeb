from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView, UpdateView, TemplateView
from distributors.models import Model, CarShop, Seller, Customer, Person
from distributors.views import ModelList, SellerList, PersonList, PersonDetail, SellerDetail, CustomerList, CustomerDetail, CarShopList, \
    ModelDetail, CarShopDetail

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(
            template_name="distributors/home_page.html"),
        name="Principal"),

    url(r'^model/$',
        ModelList.as_view(
            context_object_name='latest_model_list',
            template_name='distributors/model_list.html'),
        name='model_list'),

    url(r'^model/(?P<pk>\d+)/$',
        ModelDetail.as_view(
            model=Model,
            template_name='distributors/model_detail.html'),
        name='model_detail'),

    # url(r'^seller/$',
    #     SellerList.as_view(
    #         context_object_name='latest_seller_list',
    #         template_name='distributors/seller_list.html'),
    #     name='seller_list'),
    #
    # url(r'^seller/(?P<pk>\d+)/$',
    #     SellerDetail.as_view(
    #         model=Seller,
    #         template_name='distributors/seller_detail.html'),
    #     name='seller'),

    # url(r'^customer/$',
    #     CustomerList.as_view(
    #         context_object_name='latest_customer_list',
    #         template_name='distributors/customer_list.html'),
    #     name='customer_list'),
    #
    # url(r'^customer/(?P<pk>\d+)/$',
    #     CustomerDetail.as_view(
    #         model=Customer,
    #         template_name='distributors/customer_detail.html'),
    #     name='customer_detail'),

    url(r'^carshop/$',
        CarShopList.as_view(
            # context_object_name = 'latest_movie_list',
            model=CarShop,
            context_object_name='latest_carshop_list',
            template_name='distributors/carshop_list.html'),
        name='carshop_list'),

    url(r'^carshop/(?P<pk>\d+)/$',
        CarShopDetail.as_view(
            model=CarShop,
            template_name='distributors/carshop_detail.html'),
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
]