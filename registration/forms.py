from .models import user_mod
from django.forms import ModelForm, TextInput, PasswordInput


class user_modForm(ModelForm):
    class Meta:
        model = user_mod
        fields = ['login', 'password', 'country', 'city', 'isAdmin']
        labels = {
            "password": "*Password"
        }
        widgets = {
            'login': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'data-toggle': 'password'
            }),
            'country': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            })
        }