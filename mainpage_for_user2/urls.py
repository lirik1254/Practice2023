from django.urls import path
from . import views

urlpatterns = [
    path('mаinpage_for_user/', views.mainpage_for_user, name = 'mainpage_for_user2')
]