from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('register', views.getRegister, name='register'),
    path('login', views.getLogin, name='login'),
    path('logout', views.getLogOut, name='logout'),
]