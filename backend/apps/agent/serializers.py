from rest_framework import serializers

class AgentStateSerializer(serializers.Serializer):

    ip_fqdn = serializers.CharField(max_length=255)
    last_update = serializers.CharField(max_length=255)
    tests_performed = serializers.CharField(max_length=255)
    success_tests = serializers.CharField(max_length=255)
    unsuccess_tests = serializers.CharField(max_length=255)
    status_up = serializers.BooleanField()
    rtt_min = serializers.CharField(max_length=255)
    rtt_max = serializers.CharField(max_length=255)
    rtt_avg = serializers.CharField(max_length=255)
    rtt_std = serializers.CharField(max_length=255)
    admin_state = serializers.CharField(max_length=255)