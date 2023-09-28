from django.db import models
from .business import Business
from django.contrib.auth.models import User
from .message import MessageTemplate
from .sms_plan import SMSRate


TYPE = [('Single', 'single'), ('Bulk', 'bulk'), ('Mail', 'mail')]

class ScheduleInvitation(models.Model):
    type = models.CharField(max_length=200)
    invitation_type = models.CharField(max_length=200, blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business.name

class Invitation(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    message_template = models.ForeignKey(MessageTemplate, on_delete=models.CASCADE, blank=True, null=True)
    sms_rate = models.ForeignKey(SMSRate, on_delete=models.CASCADE, blank=True, null=True)
    schedule_invitation_id = models.IntegerField(blank=True, null=True)
    schedule_invitation_date_status_id = models.IntegerField(blank=True, null=True)
    is_schedule_invitation = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    invitation_type = models.CharField(max_length=20, choices=TYPE, default='single')
    batch = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=True) # if status is True then status = "Sent"
    invitation_code = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        fullname = "%s %s" % (self.first_name, self.last_name)
        return fullname
    
    def __str__(self):
        return self.full_name()
    
class ScheduleInvitationDate(models.Model):
    schedule_invitation = models.ForeignKey(ScheduleInvitation, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    days = models.JSONField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.schedule_invitation.business.name
    
class ScheduleInvitationDateStatus(models.Model):
    schedule_invitation = models.ForeignKey(ScheduleInvitation, on_delete=models.CASCADE)
    schedule_invitation_date = models.ForeignKey(ScheduleInvitationDate, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.schedule_invitation.business.name
    
class ScheduleInvitationData(models.Model):
    schedule_invitation = models.ForeignKey(ScheduleInvitation, on_delete=models.CASCADE)
    contacts = models.JSONField()
    email_sender_name = models.TextField(blank=True, null=True)
    email_subject = models.TextField(blank=True, null=True)
    sms_sender_id = models.TextField(blank=True, null=True)
    slug_id = models.IntegerField()
    slug = models.TextField()
    template = models.TextField()
    template_id = models.IntegerField()
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.schedule_invitation.business.name

