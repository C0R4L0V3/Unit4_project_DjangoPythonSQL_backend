from rest_framework import serializers
from .models import BlogPostSchema


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSchema
        fields = '__all__'