from django.urls import path, include
from . import views

urlpatterns = [
    path('switches', views.get_switches, name="switches"),
    path('switches/create', views.create_switch, name="switch creation"),
    path('switches/update/<str:switch_hostname>', views.update_switch, name="switch update"),
    path('switches/delete/<str:switch_hostname>', views.delete_switch, name="switch delete"),
]