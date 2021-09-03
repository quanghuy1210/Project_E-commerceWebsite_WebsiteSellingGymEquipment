from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.getHomeView, name='index'),
    path('cart', views.getCartView, name='cart'),
]