from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, TemplateView
# from models import Restaurant, Dish
# from forms import RestaurantForm, DishForm
# from views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView
from distributors.models import Model, CarShop
from distributors.views import ModelList, SellList, CustomerList, CarShopList, ModelDetail

urlpatterns = [
    # List latest 5 restaurants: /distributors/
    url(r'^$',
        TemplateView.as_view(
            template_name="distributors/home_page.html"),
            name="Principal"),

    url(r'^model/$',
    ModelList.as_view(
        context_object_name = 'latest_model_list',
        template_name = 'distributors/model_list.html'),
            name = 'model_list'),

    # url(r'^director/(?P<pk>\d+)/$',
    #     DirectorDetail.as_view(
    #         model=Director,
    #         template_name='myapp/director_detail.html'),
    #     name='director_detail'),


    url(r'^model/(?P<pk>\d+)/$',
        ModelDetail.as_view(
            model=Model,
            template_name='distributors/model_detail.html'),
            name='model_detail'),


    url(r'^seller/$',
        SellList.as_view(
            context_object_name='latest_seller_list',
            template_name='distributors/seller_list.html'),
        name='seller_list'),
    url(r'^customer/$',
        CustomerList.as_view(
            context_object_name='latest_customer_list',
            template_name='distributors/customer_list.html'),
            name='customer_list'),

    url(r'^carshop/$',
        CarShopList.as_view(
            # context_object_name = 'latest_movie_list',
            model=CarShop,
            context_object_name='latest_carshop_list',
            template_name='distributors/carshop_list.html'),
            name='carshop_list')





    #
    # # Restaurant details, ex.: /distributors/restaurants/1/
    # url(r'^restaurants/(?P<pk>\d+)/$',
    #     RestaurantDetail.as_view(),
    #     name='restaurant_detail'),
    #
    # # Restaurant dish details, ex: /distributors/restaurants/1/dishes/1/
    # url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
    #     DetailView.as_view(
    #         model=Dish,
    #         template_name='distributors/dish_detail.html'),
    #     name='dish_detail'),
    #
    # # Create a restaurant, /distributors/restaurants/create/
    # url(r'^restaurants/create/$',
    #     RestaurantCreate.as_view(),
    #     name='restaurant_create'),
    #
    # # Edit restaurant details, ex.: /distributors/restaurants/1/edit/
    # url(r'^restaurants/(?P<pk>\d+)/edit/$',
    #     LoginRequiredCheckIsOwnerUpdateView.as_view(
    #         model=Restaurant,
    #         form_class=RestaurantForm),
    #     name='restaurant_edit'),
    #
    # # Create a restaurant dish, ex.: /distributors/restaurants/1/dishes/create/
    # url(r'^restaurants/(?P<pk>\d+)/dishes/create/$',
    #     DishCreate.as_view(),
    #     name='dish_create'),
    #
    # # Edit restaurant dish details, ex.: /distributors/restaurants/1/dishes/1/edit/
    # url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/edit/$',
    #     LoginRequiredCheckIsOwnerUpdateView.as_view(
    #         model=Dish,
    #         form_class=DishForm),
    #     name='dish_edit'),
    #
    # # Create a restaurant review, ex.: /distributors/restaurants/1/reviews/create/
    # url(r'^restaurants/(?P<pk>\d+)/reviews/create/$',
    #     review,
    #     name='review_create'),
]
