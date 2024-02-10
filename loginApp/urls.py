from django.urls import path
from loginApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.account_logout, name='account_logout'),
    
]