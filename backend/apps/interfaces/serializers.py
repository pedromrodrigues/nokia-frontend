from rest_framework import serializers

class InterfaceSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=255)
    admin_state = serializers.CharField(max_length=255)
    oper_state = serializers.CharField(max_length=255)
    oper_down_reason = serializers.CharField(max_length=255)