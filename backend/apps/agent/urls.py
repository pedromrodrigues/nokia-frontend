from django.urls import path, include
from . import views

urlpatterns = [
    path('agentconfig/<str:hostname>', views.get_agent_config, name="agentconfig"),
    path('agentstate/<str:hostname>', views.get_agent_state, name="agentstate"),
    path('agentstate/<str:hostname>/run', views.set_agent_running, name="agentrunning"),
]