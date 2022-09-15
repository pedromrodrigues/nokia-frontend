from rest_framework import serializers

class ContainerSerializer(serializers.Serializer):
    
    container_id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    ip_address = serializers.CharField(max_length=255)
    ip6_address = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)  