from ..models.social_link import SocialLink
from rest_framework import serializers
from django.contrib.auth.models import User
from aormobile.models.business import BusinessIndustry, Business
from aormobile.models.user_model import UserAdditionalInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAdditionalInfo
        fields = '__all__'

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'

class BusinessIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessIndustry
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'