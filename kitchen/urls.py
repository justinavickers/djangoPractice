from django.urls import path
from . import views


urlpatterns = [

   path('', views.fridge_list, name='fridge_list'),

]