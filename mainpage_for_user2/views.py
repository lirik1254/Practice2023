from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def mainpage_for_user(request):
    return render(request, 'mainpage_for_user2/mainpage_for_user2.html')