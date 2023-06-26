from django.contrib import admin
from .models import user_mod, devices_mod, users_devices_mod

admin.site.register(user_mod)
admin.site.register(devices_mod)
admin.site.register(users_devices_mod)

