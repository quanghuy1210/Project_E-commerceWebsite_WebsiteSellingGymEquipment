from django.urls import path
from . import views
app_name = 'team'
urlpatterns = [ 
    path('', views.getteamView, name='team_view'),
]