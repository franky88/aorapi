from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SocialLink(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.URLField()
    options = models.JSONField(blank=True, null=True)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name.title()