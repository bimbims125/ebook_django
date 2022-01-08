from django.urls import path
from main import views

urlpatterns = [
    path(r'', views.home2, name='home2'),
    path(r'registers/', views.registers, name='registers'),
    path(r'logins/', views.logins, name='logins'),
]
