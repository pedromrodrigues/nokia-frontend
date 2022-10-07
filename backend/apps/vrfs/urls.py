from django.urls import path, include
from . import views

urlpatterns = [
    path('vrfs/<str:container>/<str:vrf>', views.get_net_instances, name="vrfs"),
    path('vrfs/config/<str:container>/<str:vrf_name>', views.get_vrf_config, name="vrf_config")
]