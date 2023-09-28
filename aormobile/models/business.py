from django.db import models
from django.contrib.auth.models import User
from .social_link import SocialLink


class BusinessIndustry(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "business industries"

    def __str__(self):
        return self.name

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_industry = models.ForeignKey(BusinessIndustry, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)
    current_credits = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=40, blank=True, null=True)
    google_calendar_link = models.CharField(max_length=200, blank=True, null=True)
    email_sender_name = models.CharField(max_length=200, blank=True, null=True)
    email_subject = models.CharField(max_length=200, blank=True, null=True)
    sms_sender_id = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'businesses'

    def __str__(self):
        return self.name
    
class BusinessLink(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)
    notification_email = models.EmailField(blank=True, null=True)
    links = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name

class BusinessContent(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    rating_threshold = models.IntegerField(default=0)
    contents = models.TextField(blank=True, null=True)
    rating_label = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name
    
class BusinessSetup(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    tagline = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    brand_color = models.CharField(max_length=200, blank=True, null=True)
    other_settings = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name
    
class BusinessSocialLink(models.Model):
    business_link = models.ForeignKey(BusinessLink, on_delete=models.CASCADE)
    social_link = models.ForeignKey(SocialLink, on_delete=models.CASCADE)
    business_url = models.URLField()
    status = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_link.business.name

class BusinessReview(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    rating = models.IntegerField()
    business_social_link = models.ForeignKey(BusinessSocialLink, on_delete=models.CASCADE)
    review_content = models.TextField(blank=True, null=True)
    invitation_code = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guest_name

class BusinessShortURL(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    url = models.URLField()
    code = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name