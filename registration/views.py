from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import user_modForm
from .models import user_mod
from django.contrib import messages

login = ''


def registration(request):
    error = ''
    if request.method == 'POST':
        form = user_modForm(request.POST)
        if form.is_valid():
            isOk_login = True
            isOk_admin = form.cleaned_data.get("isAdmin")
            isContinueAdmin = True
            login = form.cleaned_data.get("login")
            if login == "user2":
                return redirect('contregsecuser')
            all_users = user_mod.objects.all()
            for i in all_users:
                if i.login == login:
                    isOk_login = False
                if i.isAdmin == True and isOk_admin == True:
                    isContinueAdmin = False
            if isOk_login and isContinueAdmin:
                if isOk_admin:
                    form.save()
                    messages.success(request, message='Регистрация прошла успешно')
                    return redirect('authorisation')
                else:
                    password = form.cleaned_data.get("password")
                    country = form.cleaned_data.get("country")
                    city = form.cleaned_data.get("city")
                    isAdmin = False
                    data = {
                        'login': login,
                        'password': password,
                        'country': country,
                        'city': city,
                        'isAdmin': isAdmin
                    }
                    return redirect('continueregistration')
            else:
                if not isOk_login:
                    error = "Такой логин уже зарегистрирован!"
                else:
                    error = "В системе уже есть администратор!"
        else:
            error = "Форма была неверной"
    form = user_modForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration_page.html', data)


def continueregistration(request):
    if request.method == "POST":
        login = request.POST['login']
        password = request.POST['password']
        city = request.POST['city']
        country = request.POST['country']
        data = {
            'login': login,
            'password': password,
            'city': city,
            'country': country
        }
        return render(request, 'mainpage_for_user/mainpage_for_user.html', data)
    return render(request, 'registration/continue_registration_page.html')
