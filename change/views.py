from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def change(request):
    return render(request, 'change/change_data.html')