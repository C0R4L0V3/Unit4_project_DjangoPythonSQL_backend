from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from rest_framework import generics
from profiles_api.serializers import ProfileSerializer # imports the profile serializer
from profiles_api.models import Profile

# Create your views here.
# API view to register
class RegisterUserAPIView(APIView):
    def post(self, request):
        

        #serialize user data
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            #saves the user and gets the instance
            user = user_serializer.save()
            #create and save a profile
            profile, created = Profile.objects.get_or_create(
                    user=user,
                    defaults={
                        'bio': "This user has not added a bio.",
                        'profile_picture': 'profile_picture/profile_picture_placeholder.jpg'
                    }
                )
            #serialize the profile data
            profile_serializer = ProfileSerializer(profile)

            return Response({
                "message": "User created successfully.",
                'user': user_serializer.data, #user data
                'profile': profile_serializer.data #profile data
                }, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# API view to log in a user
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        
            # fetch or create - profile if it exsists, allowing me to capture and connect both the user and profile data on login
            profile = user.profile if hasattr(user, 'profile') else None
            if not profile:
                profile = Profile.objects.create(
                    user=user,
                    bio="This user has not added a bio.",
                    profile_picture='profile_picture/profile_picutre_placeholder.jpg'
                )
            profile_data = ProfileSerializer(profile).data
            user_data = UserSerializer(user).data
     
            return Response({
                'message': 'Login successful!',
                'user': user_data,
                'profile': profile_data
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

#Custom logout view
class CustomLogoutView(LogoutView):
    next_page = '/' # redirects after logout

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
