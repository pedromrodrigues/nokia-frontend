from django.urls import path
from . import views

urlpatterns = [
    path('agentconfig/<str:hostname>',
         views.get_agent_config, name="agentconfig"),
    path('agentstate/<str:hostname>', views.get_agent_state, name="agentstate"),
    path('agentstate/<str:hostname>/run',
         views.set_agent_running, name="agentrunning"),
    path('agentstate/<str:hostname>/adminstate',
         views.get_agent_admin_state, name="agent admin state"),
    path('agentstate/<str:hostname>/adminstate/set',
         views.set_agent_admin_state, name="agent admin state set"),
    path('agentstate/<str:hostname>/test/adminstate/set',
         views.set_agent_test_admin_state, name="agent test admin state"),
    path('agentstate/<str:hostname>/test/delete',
         views.delete_agent_test, name="delete agent test"),
]
