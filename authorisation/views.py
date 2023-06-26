from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from registration.models import user_mod
from django.contrib import messages


def authorisation(request):
    if request.method == 'POST':
        login = request.POST['login_from_form']
        password = request.POST['password_from_form']
        all_users = user_mod.objects.all()
        isOk = False
        for i in all_users:
            if login == i.login and password == i.password:
                isOk = True
        if isOk:
            man = user_mod.objects.get(login=login)
            if man.isAdmin:
                return redirect('mainpage_for_admin')
            else:
                return redirect('mainpage_for_user')
        else:
            messages.success(request, message='Неверный логин или пароль')
    return render(request, 'authorisation/authorisation_page.html')
