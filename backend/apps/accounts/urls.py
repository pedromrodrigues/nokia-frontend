from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/user', views.get_my_user, name="accounts/user"),
]