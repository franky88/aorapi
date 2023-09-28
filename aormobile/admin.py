from django.contrib import admin
from .models.social_link import SocialLink
from .models.user_model import UserAdditionalInfo
from .models.business import Business, BusinessLink, BusinessContent, BusinessSetup, BusinessSocialLink, BusinessReview, BusinessIndustry, BusinessShortURL
from .models.message import MessageTemplate
from .models.contact import Contact
from .models.invitation import Invitation, ScheduleInvitation, ScheduleInvitationDate, ScheduleInvitationDateStatus, ScheduleInvitationData
from .models.mail_setting import MailSetting
from .models.sms_plan import SMSPlan, SMSSubcription, SMSRate
from .models.credit_transaction import CreditTransaction
from .models.history import ReminderEmailHistory
from .models.aws import AWS
from .models.sns import SNSTopic, SNSTopicSubscription
from .models.mobile import MobileMessage

# Register your models here.
admin.site.register(SocialLink)
admin.site.register(UserAdditionalInfo)
admin.site.register(Business)
admin.site.register(BusinessLink)
admin.site.register(BusinessContent)
admin.site.register(BusinessSetup)
admin.site.register(BusinessSocialLink)
admin.site.register(BusinessReview)
admin.site.register(BusinessIndustry)
admin.site.register(BusinessShortURL)

admin.site.register(MessageTemplate)

admin.site.register(Contact)

admin.site.register(Invitation)
admin.site.register(ScheduleInvitation)
admin.site.register(ScheduleInvitationDate)
admin.site.register(ScheduleInvitationDateStatus)
admin.site.register(ScheduleInvitationData)

admin.site.register(MailSetting)

admin.site.register(SMSPlan)
admin.site.register(SMSSubcription)
admin.site.register(SMSRate)

admin.site.register(CreditTransaction)

admin.site.register(ReminderEmailHistory)

admin.site.register(AWS)

admin.site.register(SNSTopic)
admin.site.register(SNSTopicSubscription)

admin.site.register(MobileMessage)