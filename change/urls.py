from django.urls import path
from . import views

urlpatterns = [
    path('', views.change, name = 'change_data'),
]