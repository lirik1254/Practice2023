from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def contregsecuser(request):
    return render(request, 'continue_registration_for_user2/continue_registration_for_user2.html')
