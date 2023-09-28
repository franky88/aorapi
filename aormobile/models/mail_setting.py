from django.db import models
from django.contrib.auth.models import User


class MailSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    email = models.EmailField()
    confirmation_template = models.IntegerField(blank=True, null=True)
    sms_confirmation_template = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username