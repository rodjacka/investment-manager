from rest_framework import routers
from datamanager.viewsets import SecurityViewSet

router = routers.DefaultRouter()
router.register(r'security', SecurityViewSet)