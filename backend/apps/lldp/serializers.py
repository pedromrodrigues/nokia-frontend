from rest_framework import serializers

class LldpSerializer(serializers.Serializer):

    iface_name = serializers.CharField(max_length=255)
    neighbor_id = serializers.CharField(max_length=255)
    neighbor_first_message = serializers.CharField(max_length=255)
    neighbor_last_update = serializers.CharField(max_length=255)
    neighbor_name = serializers.CharField(max_length=255)
    neighbor_iface = serializers.CharField(max_length=255)