from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('upload/', views.up, name='mainpage'),
]
