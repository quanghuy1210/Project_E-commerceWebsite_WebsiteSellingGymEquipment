from django.urls import path
from . import views
from .views import Promotions_Product

app_name = 'promotions'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:id_category>', views.Promotions_Product, name='product'),
    # path('chitiet/<int:id_category>', views.chitiet , name = 'chitiet'),
]