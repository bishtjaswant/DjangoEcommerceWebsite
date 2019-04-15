from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/', views.contactus, name="contactus"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('products/', views.products, name="products"),
    path('checkout/', views.checkout, name="checkout"),
]
