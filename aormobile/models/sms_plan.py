from django.db import models
from .business import Business


class SMSPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True)
    slug = models.SlugField()
    capacity = models.FloatField()
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SMSSubcription(models.Model):
    credits = models.FloatField(blank=True, null=True)
    fee_per_message = models.FloatField(default=0.7)
    is_active = models.BooleanField(default=True)
    is_renewal = models.BooleanField(default=False)
    is_upgrade = models.BooleanField(default=False)
    is_downgrade = models.BooleanField(default=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    sms_plan = models.ForeignKey(SMSPlan, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=100, default="topup")
    payer_id = models.CharField(max_length=200, blank=True, null=True)
    payment_id = models.CharField(max_length=200, blank=True, null=True)
    token = models.CharField(max_length=200, blank=True, null=True)
    chargebee_plan_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.business.name
    
class SMSRate(models.Model):
    country_or_region = models.CharField(max_length=200)
    iso_code = models.CharField(max_length=100)
    rate = models.FloatField()
    area_code = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_or_region