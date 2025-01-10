from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import BlogPostSerializer
from .models import BlogPostSchema

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPostSchema.objects.all().order_by('id')
    serializer_class = BlogPostSerializer

# class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPostSchema.objects.all().order_by('id')
#     serializer_class = BlogPostSerializer