from django.db import models


class AWS(models.Model):
    credit_limit = models.FloatField()
    sms_credit = models.FloatField()
    remaining_credit = models.FloatField()
    about_to_reach_reminder = models.BooleanField(default=False)
    is_reached_reminder = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)