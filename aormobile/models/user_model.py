from django.db import models
from django.contrib.auth.models import User


class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    address = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username