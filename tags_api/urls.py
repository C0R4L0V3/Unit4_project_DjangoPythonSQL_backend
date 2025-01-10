from rest_framework.routers import DefaultRouter
from .views import TagViewSet
# from django.urls import path, include

router = DefaultRouter()
router.register(r'', TagViewSet) # Register the viewset to the router

urlpatterns = router.urls
