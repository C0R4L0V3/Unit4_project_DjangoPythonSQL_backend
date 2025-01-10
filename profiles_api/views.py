from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all().order_by('id')
#     serializer_class = ProfileSerializer