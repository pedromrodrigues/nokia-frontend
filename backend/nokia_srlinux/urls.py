from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('apps.container.urls')),
    path('api/v1/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.interfaces.urls')),
    path('api/v1/', include('apps.vrfs.urls')),
    path('api/v1/', include('apps.lldp.urls')),
    path('api/v1/', include('apps.agent.urls')),
    path('api/v1/', include('apps.switch.urls'))
]
