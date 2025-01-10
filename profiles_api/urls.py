from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
# from django.urls import path, include

router = DefaultRouter()
router.register(r'', ProfileViewSet)

urlpatterns = router.urls