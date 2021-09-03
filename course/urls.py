from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.getCourseView, name='course_view'),
    path('course/<int:id_loaimon>', views.getLoaimontapluyenView,
         name='loai_mon_tap_luyen_view'),
    
]
