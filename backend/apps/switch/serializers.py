from rest_framework import serializers
from .models import Switch

class SwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switch
        read_only_fields = (
            "created_at",
            "created_by",
        ),
        fields = (
            "hostname",
            "name",
            "port",
            "ipv4",
            "ipv6",
            "switch_type"
        )