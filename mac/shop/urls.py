from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="Tracking Status"),
    path('search/', views.search, name="Search"),
    path('productView/', views.productView, name="Product View"),
    path('checkout/', views.checkout, name="CheckOut"),
]
