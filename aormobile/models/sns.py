from django.db import models
from django.contrib.auth.models import User


class SNSTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_arn = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class SNSTopicSubscription(models.Model):
    sns_topic = models.ForeignKey(SNSTopic, on_delete=models.CASCADE)
    endpoint_arn = models.CharField(max_length=200)
    subscription_arn = models.CharField(max_length=200, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sns_topic