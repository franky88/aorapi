from django.db import models
from django.contrib.auth.models import User


class MessageTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=True)
    message_type = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name