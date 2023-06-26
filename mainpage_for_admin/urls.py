from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name = 'mainpage_for_admin')
]