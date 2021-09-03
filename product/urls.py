from django.urls import path
from . import views
from .views import ProductDetail

app_name = 'product'
urlpatterns = [
    path('', views.getProductView, name='product_view'),
    # path('detail/<int:id_product>', views.getProductDetailsView, name='product_detail'),
    path('detail/<int:id_product>', ProductDetail.as_view(), name='product_detail'),
    path('type/<int:id_category>', views.getProductTypeView, name='product_type'),
    path('search/', views.searchProduct, name='product_search'),
]