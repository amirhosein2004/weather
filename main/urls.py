from django.urls import path
from . import views

urlpatterns = [
    path('', views.BaseWeatherView.as_view(), name='home'),
]