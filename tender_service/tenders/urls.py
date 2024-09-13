from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BidViewSet, OrganizationViewSet, TenderViewSet, ping

router = DefaultRouter()
router.register(r'tenders', TenderViewSet, basename='tender')
router.register(r'bids', BidViewSet, basename='bid')
router.register(r'organizations', OrganizationViewSet, basename='organization')

urlpatterns = [
    path('ping/', ping, name='ping'),
    path('', include(router.urls)),
]