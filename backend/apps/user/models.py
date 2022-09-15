from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    org_number = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField()

    def __str__(self):
        return '%s' % self.name
