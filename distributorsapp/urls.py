"""distributorsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # url(r'^login/', login, name='login'),
    # url(r'^logout/', logout, name='logout'),
    #
    url(r'^admin/', include(admin.site.urls)),
    url(r'^distributors/', include('distributors.urls', namespace='distributors')),
   # url(r'^login/$', auth_views.LoginView.as_view(authentication_form=AuthenticationFormWithChekUsersStatus)),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^', include('distributors.urls', namespace='distributors')),

]

#if settings.DEBUG:
# Used even in production though not recommended: https://devcenter.heroku.com/articles/s3-upload-python
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
]
