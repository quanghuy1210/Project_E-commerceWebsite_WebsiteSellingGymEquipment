from django.urls import path
from . import views
from .views import CheckOut

app_name = 'order'
urlpatterns = [
    path('checkout', CheckOut.as_view(), name='checkout'),
]