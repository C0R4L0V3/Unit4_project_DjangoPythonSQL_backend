from rest_framework.routers import DefaultRouter
from .views import BlogViewSet
# from django.urls import path, include

router = DefaultRouter()
router.register(r'blogposts', BlogViewSet, basename='blogpost')

urlpatterns = router.urls