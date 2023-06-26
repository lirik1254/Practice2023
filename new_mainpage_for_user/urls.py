from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_mainpage_for_user, name = 'new_mainpage_for_user')
]