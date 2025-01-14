from django.urls import path
from .views import RegisterUserAPIView, LoginAPIView, CustomLogoutView, UserList, UserDetail, UpdateUserProfileView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('profile/update/', UpdateUserProfileView.as_view(), name='update_profile'),
]