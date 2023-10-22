
from django.contrib.sites import requests
from django.urls import include, path

from rest_framework import routers
from . import views

from fileupload import views

urlpatterns = [
    path('share/', views.share)
]
