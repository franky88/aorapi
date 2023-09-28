from django.urls import path, include
from rest_framework import routers
from aormobile.api.views import SocialLinkViewSets, BusinessIndustryViewSets, UserViewSets, UserAdditionalInfoViewSets, BusinessViewSets

router = routers.DefaultRouter()
router.register(r'social-links', SocialLinkViewSets)
router.register(r'business', BusinessViewSets)
router.register(r'business-industry', BusinessIndustryViewSets)
router.register(r'users', UserViewSets)
router.register(r'users/informations', UserAdditionalInfoViewSets)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]