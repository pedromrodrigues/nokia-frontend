from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

#router = DefaultRouter()
#router.register("containers", get_containers, basename="containers")

urlpatterns = [
    path('containers', views.get_containers, name="containers"),
]