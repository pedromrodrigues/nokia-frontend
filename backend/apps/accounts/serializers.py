from rest_framework import serializers

class MyUserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    is_staff = serializers.BooleanField()
    name = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    last_login = serializers.CharField(max_length=255)
    date_joined = serializers.CharField(max_length=255)

    