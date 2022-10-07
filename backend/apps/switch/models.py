from django.db import models
from django.contrib.auth.models import User

class Switch(models.Model):
    hostname = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    switch_type = models.CharField(max_length=255)
    port = models.IntegerField()
    ipv4 = models.GenericIPAddressField(protocol="IPv4")
    ipv6 = models.GenericIPAddressField(protocol="IPv6", blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="switches", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.name
    
