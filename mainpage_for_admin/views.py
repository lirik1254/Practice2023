from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def mainpage(request):
    return render(request, 'mainpage_for_admin/mainpage_for_admin.html')

