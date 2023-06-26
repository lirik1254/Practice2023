from django.db import models


class user_mod(models.Model):
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)
    country = models.CharField('Страна', max_length=50)
    city = models.CharField('Город', max_length=50)
    isAdmin = models.BooleanField('Администратор?')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'


class devices_mod(models.Model):
    name = models.CharField('Название', max_length=50)
    floor = models.CharField('Этаж', max_length=50, default = "null")
    room = models.CharField('Комната', max_length=50, default = 'null')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class users_devices_mod(models.Model):
    user_id = models.ForeignKey(user_mod, on_delete=models.CASCADE)
    device_id = models.ForeignKey(devices_mod, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь-устройство'
        verbose_name_plural = 'Пользователи-устройства'
