from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_list, name='catalog_product_list'),
    path('<int:slug>', views.category, name='category'),

]
