from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorisation.urls')),
    path('registration/', include('registration.urls')),
    path('mainpage_for_admin/', include('mainpage_for_admin.urls')),
    path('mainpage_for_user/', include('mainpage_for_user.urls')),
    path('change_data/', include('change.urls')),
    path('mainpagе_for_user/', include('new_mainpage_for_user.urls')),
    path('mainpage_for_usеr/', include('user2.urls')),
                  #Тут е русская первая
    path('change_data_admin/', include('change_data_admin.urls')),
    path('changе_data_admin/', include('change_data_admin2.urls')),
    path('rеgistrаtion/continuеrеgistrаtion/', include('continue_registration_for_user2.urls')),
    path('mаinраge_for_user/', include('mainpage_for_user2.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
