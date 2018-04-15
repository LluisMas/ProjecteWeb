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

    url(r'^admin/', admin.site.urls),
    url(r'^$', include('distributors.urls', namespace='distributors')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
]

#if settings.DEBUG:
# Used even in production though not recommended: https://devcenter.heroku.com/articles/s3-upload-python
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
]
