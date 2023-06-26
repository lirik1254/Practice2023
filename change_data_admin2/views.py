from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def change_data_admin2(request):
    return render(request, 'change_data_admin2/change_data_admin2.html')
