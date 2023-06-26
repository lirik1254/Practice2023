from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def mainpage(request):
    return render(request, 'mainpage_for_user/mainpage_for_user.html')



