from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import SocialLinkSerializer, UserSerializer, BusinessIndustrySerializer, UserAdditionalInfoSerializer, BusinessSerializer
from aormobile.models.social_link import SocialLink
from aormobile.models.business import BusinessIndustry, Business
from django.contrib.auth.models import User
from aormobile.models.user_model import UserAdditionalInfo

# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserAdditionalInfoViewSets(viewsets.ModelViewSet):
    queryset = UserAdditionalInfo.objects.all()
    serializer_class = UserAdditionalInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

class SocialLinkViewSets(viewsets.ModelViewSet):
    """
    API endpoint that allows social link to be viewed or edited.
    """
    queryset = SocialLink.objects.all().order_by('site_name')
    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusinessIndustryViewSets(viewsets.ModelViewSet):
    """
    API endpoint that allows social link to be viewed or edited.
    """
    queryset = BusinessIndustry.objects.all()
    serializer_class = BusinessIndustrySerializer
    permission_classes = [permissions.IsAuthenticated]

class BusinessViewSets(viewsets.ModelViewSet):
    """
    API endpoint that allows social link to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]