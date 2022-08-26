from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.share_communities, name='communities')
]
