from django.db import models
from django.contrib.auth.models import User
from aormobile.models.business import BusinessReview


class MobileMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_review = models.ForeignKey(BusinessReview, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_review.business.name