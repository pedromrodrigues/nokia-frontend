from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('interfaces/<str:container>', views.get_interfaces, name="interfaces"),
    path('interfaces/config/<str:container>/<path:iface_name>', views.get_interface_config, name="interfaces_config")
]