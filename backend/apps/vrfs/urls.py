from django.urls import path
from . import views

urlpatterns = [
    path('vrfs/<str:hostname>/<str:vrf>', views.get_net_instances, name="vrfs"),
    path('vrfs/config/<str:hostname>/<str:vrf_name>', views.get_vrf_config, name="vrf_config")
]