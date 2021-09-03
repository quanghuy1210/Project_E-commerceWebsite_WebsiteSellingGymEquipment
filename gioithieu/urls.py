from django.urls import path
from . import views

app_name = 'gioithieu'
urlpatterns = [
    path('', views.getgioithieuView, name='gioithieu_view'),
]