from django.db import models
from .business import Business


class CreditTransaction(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    credits = models.FloatField()
    requested_by = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    attachment_filename = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name
    