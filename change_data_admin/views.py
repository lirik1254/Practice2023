from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def change_data_admin(request):
    return render(request, 'change_data_admin/change_data_admin.html')


