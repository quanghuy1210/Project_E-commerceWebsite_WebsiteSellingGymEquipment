from django.urls import path
from . import views

app_name = 'tintuc' 
urlpatterns = [
    path('', views.gettintucView, name='tintuc_view'),
     path('chitiet/<int:id_tintuc>', views.getloaitintucView, name='loai_tin_view'),
]