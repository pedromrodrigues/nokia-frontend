from django.urls import path, include
from . import views

urlpatterns = [
    path('lldp/<str:container>', views.get_lldp_neighbors, name="lldp"),
]