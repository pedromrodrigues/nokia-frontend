from django.urls import path
from . import views

urlpatterns = [
    path('lldp/<str:hostname>', views.get_lldp_neighbors, name="lldp"),
]