from rest_framework.routers import DefaultRouter
from .views import ProfileView
from .views import ProfileDetail

from . import views
from django.urls import path, include

urlpatterns = [
    path('profiles/', views.ProfileView.as_view(), name='profile'),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail')
]

# router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet, basename='profile')

# urlpatterns = router.urls
4

# ProfileViewSet