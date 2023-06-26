from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def user2(request):
    return render(request, 'user2/user2.html')

