from django.db import models
from .business import Business
from .invitation import Invitation


class ReminderEmailHistory(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    is_primary_reminder_sent = models.BooleanField(default=False)
    is_secondary_reminder_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.business.name
    
class CustomerReminderHistory(models.Model):
    group = models.BigIntegerField()
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invitation