from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('servicing/<int:id>', views.car_detail, name="car_detail")
   
  ]