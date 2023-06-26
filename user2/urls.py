from django.urls import path
from . import views

urlpatterns = [
    path('', views.user2, name = 'user2')
]