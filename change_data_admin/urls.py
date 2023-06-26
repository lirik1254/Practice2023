from django.urls import path
from . import views


urlpatterns = [
    path('', views.change_data_admin, name = 'change_data_admin')
]