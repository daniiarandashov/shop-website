from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
    
]