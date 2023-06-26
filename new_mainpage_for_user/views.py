from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def new_mainpage_for_user(request):
    return render(request, 'new_mainpage_for_user/new_mainpage_for_user.html')
# Create your views here.
