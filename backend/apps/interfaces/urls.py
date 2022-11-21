from django.urls import path
from . import views

urlpatterns = [
    path('interfaces/<str:hostname>', views.get_interfaces, name="interfaces"),
    path('interfaces/config/<str:hostname>/<path:iface_name>', views.get_interface_config, name="interfaces_config")
]